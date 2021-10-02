from flask_sqlalchemy_session import flask_scoped_session
from db_engine import session_factory
from app import app

db_session = flask_scoped_session(session_factory,app)
