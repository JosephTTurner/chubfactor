from dotenv import load_dotenv
from os import urandom, getenv

load_dotenv()

DEBUG = bool(getenv("DEBUG"))

DB_SCHEMA = getenv("DB_SCHEMA")
DB_PORT = getenv("DB_PORT")
DB_DIALECT = getenv("DB_DIALECT")
DB_HOST = getenv("DB_HOST")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")
SECRET_KEY = urandom(32)
