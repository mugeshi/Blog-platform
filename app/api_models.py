from flask_restx import fields
from .extensions import api

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

# Model for user search history
user_history_model = api.model("User History", {
    "id": fields.Integer,
    "name": fields.String,
    "search_date": fields.DateTime
})

# Model for sign-up request
req_signup_model = api.model("Sign Up Request", {
    "username": fields.String,
    "email": fields.String,
    "password": fields.String
})

# Model for login response
res_login_model = api.model("Log In Response", {
    "access_token": fields.String
})from flask_restx import fields
from .extensions import api

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

# Model for user search history
user_history_model = api.model("User History", {
    "id": fields.Integer,
    "name": fields.String,
    "search_date": fields.DateTime
})

# Model for sign-up request
req_signup_model = api.model("Sign Up Request", {
    "username": fields.String,
    "email": fields.String,
    "password": fields.String
})

# Model for login response
res_login_model = api.model("Log In Response", {
    "access_token": fields.String
})

# Model for search request
req_search_model = api.model("Search Request", {
    "query": fields.String(description="Search query string")
})

# Model for user profile details
profile_details_model = api.model("Profile Details", {
    "username": fields.String(description="Username"),
    "email": fields.String(description="User email"),
    "password": fields.String(description="User password")
})



