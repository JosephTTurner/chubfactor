'''
Main application
'''
from flask import Flask
from webapp.webapp import webapp_blueprint

app = Flask(__name__)
app.register_blueprint(webapp_blueprint)

def main():
    '''
    main / parent process of application
    '''
    app.run(host="127.0.0.1", port=5000, debug=True, load_dotenv=True)

if __name__ == "__main__":
    main()
