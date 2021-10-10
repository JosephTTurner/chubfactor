from flask import Flask
from app import webapp_blueprint
from core import core_blueprint
from core.config.config import SECRET_KEY


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.register_blueprint(core_blueprint)
    app.register_blueprint(webapp_blueprint)

    return app
