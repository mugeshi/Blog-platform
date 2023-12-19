from flask import Flask
from flask_restx import Api, Resource
from api_models import profile_details_model,user_updated_profile_model, req_signup_model, SearchHistory, req_login_model,user_history_model,req_history_model
from extensions import api, db
from flask_bcrypt import generate_password_hash 
from model import User 
import requests
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt


profile_ns = api.namespace('profile', description='Create, update or delete user profile')
blog_ns = api.namespace('blogs', description='Blog posts')
login_ns = api.namespace('login', description='Handle user log in')
search_ns = api.namespace('search', description='Users to find specific content within the blog platform')
history_ns = api.namespace('history', description='Get, update or delete user history')



@profile_ns.route('')
class profile(Resource):

    @jwt_required()
    @profile_ns.marshall_with(profile_details_model)
    def get(self):
        """
        Get the user account details
        """
        user_details = get_jwt_identity()
        user = User.query.filter_by(id = user_details["id"]).first()

        return user
    

    @profile_ns.expect(req_signup_model)
    def post(self):
        """
        Create a user account
        """
        data = profile_ns.payload

        username =  data["username"]
        email = data["email"]
        password = data["password"]

        user = User.query.filter_by(email = data["email"]).first()

        if not user:
            new_user = User(username=username, email=email, password_hash = password)
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'New user added successfully.'}, 201
        else:
            return {'message': 'User already exists.'}, 422
        
        
    @jwt_required()
    @profile_ns.expect(user_updated_profile_model)
    @profile_ns.marshal_with(user_updated_profile_model)
    def put(self):
        """
        Update a user account
        """
        user_details = get_jwt_identity()
        user = User.query.filter_by(id = user_details["id"]).first()
        
        # Update account details for the user
        user.username = profile_ns.payload["username"]
        user.password_hash = profile_ns.payload["password"]
        db.session.commit()
        return user
    

    @jwt_required()
    def delete(self):
        """
        Delete a user account
        """
        user_details = get_jwt_identity()
        user = User.query.filter_by(email = user_details["email"]).first()
        
        if not user:
            return {"message": "User not found"}, 404
        
        # Delete all history data for the user
        search_items = SearchHistory.query.filter_by(user_id = user.id).all()
        for item in search_items:
            db.session.delete(item)
        db.session.commit()
        
        # Delete user account
        db.session.delete(instance=user)
        db.session.commit()
        return {}, 204
    

    @login_ns.route('')
    class LogIn(Resource):
    
     @login_ns.expect(req_login_model)
     def post(self):
        """
        Log In user and return a JWT token
        """
        data = login_ns.payload
        
        email = data["email"]
        password = data["password"]
        
        user = User.query.filter_by(email = email).first()
        
        if user and user.authenticate(password):
            access_token = create_access_token(identity={'id': user.id, 'email': email})
            return {'access_token': access_token}, 200
        else:
            return {"message": "Invalid email or password"}, 401
    
        
@history_ns.route('')
class History(Resource):
    
    @jwt_required()
    @history_ns.marshal_list_with(user_history_model)
    def get(self):
        """
        Get search history for a user
        """
        user_details = get_jwt_identity()
        user = User.query.filter_by(email = user_details["email"]).first()
        return SearchHistory.query.filter_by(user_id = user.id).all()
    
    @jwt_required()
    @history_ns.expect(req_history_model)
    @history_ns.marshal_with(user_history_model)
    def post(self):
        """
        Add search query to the search history database
        """
        user_details = get_jwt_identity()
        user = User.query.filter_by(email = user_details["email"]).first()
        
        new_search_query = SearchHistory(
            user_id = user.id,
            name = history_ns.payload['query']
        )
        db.session.add(new_search_query)
        db.session.commit()
        
        return new_search_query, 201
    
@history_ns.route('/<int:id>')
class History(Resource):
    
    @jwt_required()
    def delete(self, id):
        """
        Delete a search history item from history using the id
        """
        user_details = get_jwt_identity()
        user = User.query.filter_by(email = user_details["email"]).first()
        search_item = SearchHistory.query.filter_by(id = id, user_id = user.id).first()
        
        if not search_item:
            return {"message": "Not Found. The resource does not exist or may have been deleted."}, 404
        
        db.session.delete(search_item)
        db.session.commit()
        return {}, 204
    
    
   
       
