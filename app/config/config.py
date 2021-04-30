from dotenv import load_dotenv
from os import environ
load_dotenv()

DB_SCHEMA=environ.get('DB_SCHEMA')
DB_PORT=environ.get('DB_PORT')
DB_DIALECT=environ.get('DB_DIALECT')
DB_HOST=environ.get('DB_HOST')
DB_USER=environ.get('DB_USER')
DB_PASS=environ.get('DB_PASS')

print(DB_HOST)
