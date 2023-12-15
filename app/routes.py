from flask import Flask
from flask_restx import Api, Resource
from api_models import blog_post_model,profile_details_model
from extensions import create_app, api
from flask_bcrypt import generate_password_hash  # Import generate_password_hash
from model import User 
import request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt


app = create_app()
api.init_app(app)


profile_ns = api.namespace('profile', description='Create, update or delete user profile')
blog_ns = api.namespace('blogs', description='Blog posts')
login_ns = api.namespace('login', description='Handle user log in')
search_ns = api.namespace('search', description='Users to find specific content within the blog platform')
signup_ns = api.namespace('signup', description='The user can be able to create an account')


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



