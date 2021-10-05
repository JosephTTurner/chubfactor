"""
Main application
"""
from flask import Flask
import jinja2
from webapp import webapp_blueprint
from core import core_blueprint
from core.config.config import DEBUG, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(core_blueprint)
app.register_blueprint(webapp_blueprint)


def main():
    """
    main / parent process of application
    """
    app.run(debug=DEBUG, load_dotenv=True)


if __name__ == "__main__":
    main()
