from flask_restx import fields
from extensions import api

# Model for a blog post
blog_post_model = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'date': fields.String,  # Date of the blog post, consider changing to DateTime if needed
    'avatar_url': fields.String,
    'category': fields.String,
    'blog_post': fields.String,
    'comment': fields.String,
    'mins': fields.Integer,
    'likes': fields.Integer,
}

# Model for user profile details
profile_details_model = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    # Add more fields as needed for the user profile
}

# Model for updating user profile details
user_updated_profile_model = {
    'username': fields.String,
    'password': fields.String,
    # Add more fields as needed for updating the user profile
}

# Model for login request
req_login_model = {
    'email': fields.String(required=True),
    'password': fields.String(required=True),
}

# Model for user history
user_history_model = {
    'id': fields.Integer,
    'name': fields.String,
    'search_date': fields.DateTime,
    # Add more fields as needed for the user history
}

# Model for history request
req_history_model = {
    'query': fields.String(required=True),
    # Add more fields as needed for adding to user history
}
