import os
from flask import Flask
from flask_cors import CORS
from extensions import api, db, migrate, bcrypt, jwt


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('sqlite:///db.bloglify')
    app.config["JWT_SECRET_KEY"] = "phase5JWTkey"
    
    api.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
