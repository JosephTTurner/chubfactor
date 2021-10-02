"""
Main application
"""
from flask import Flask
from webapp import webapp_blueprint
from config.config import DEBUG, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(webapp_blueprint)


def main():
    """
    main / parent process of application
    """
    debug=DEBUG
    app.run(debug=debug, load_dotenv=True)


if __name__ == "__main__":
    main()
