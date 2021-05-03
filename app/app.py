'''
Main application
'''
from flask import Flask
from webapp import webapp_blueprint
from config.config import DB_HOST

app = Flask(__name__)
app.register_blueprint(webapp_blueprint)

def main():
    '''
    main / parent process of application
    '''
    app.run(debug=True, load_dotenv=True)

if __name__ == "__main__":
    main()
