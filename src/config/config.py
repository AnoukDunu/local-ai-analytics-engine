# This is to configure things like database credentials, api keys, etc.
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
def get_engine():
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    # Create the database engine
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}')
    return engine