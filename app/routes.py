from flask import Flask
from flask_restx import Api, Resource
from api_models import blog_post_model
from extensions import create_app, api
import requests

app = create_app()
api.init_app(app)

blog_ns = api.namespace('blogs', description='Blog posts')
ogin_ns = api.namespace('login', description='Handle user log in')
search_ns = api.namespace('search', description=' users to find specific content within the blog platform')



