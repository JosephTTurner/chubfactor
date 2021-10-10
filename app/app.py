"""
Main application
"""
from core.config.config import DEBUG
from app.app_factory import create_app

app = None

def main():
    """
    main / parent process of application
    """
    app = create_app()
    app.run(debug=DEBUG, load_dotenv=True)
