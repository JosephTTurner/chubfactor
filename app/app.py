'''
Main application
'''
from flask import Flask
from webapp import webapp_blueprint
from config.config import SECRET_KEY

app = Flask(__name__)
app.register_blueprint(webapp_blueprint)

def main():
    '''
    main / parent process of application
    '''
    app.config['SECRET_KEY']=SECRET_KEY
    app.run(debug=True, load_dotenv=True)

if __name__ == "__main__":
    main()
