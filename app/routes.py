from flask import Flask
from flask_restx import Api, Resource
from api_models import blog_post_model,profile_details_model,user_updated_profile_model
from extensions import create_app, api, db
from flask_bcrypt import generate_password_hash  # Import generate_password_hash
from model import User 
import requests
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt


app = create_app()
api.init_app(app)


profile_ns = api.namespace('profile', description='Create, update or delete user profile')
blog_ns = api.namespace('blogs', description='Blog posts')
login_ns = api.namespace('login', description='Handle user log in')
search_ns = api.namespace('search', description='Users to find specific content within the blog platform')



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
    
   
        


