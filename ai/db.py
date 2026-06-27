# Created this db connection (which might seem redundant since the base ETL pipeline already has a similar file)
# Because ETL pipeline does batch inserts and bulk writes.
# This AI layer only does small more infrequent reads so I wanted to keep the two seperate (even though they do almost the same thing)
# This also uses the "psycopg2" import to execute queries directly into the database

import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Database configuration
def get_connection():
    return psycopg2.connect(
        host = os.getenv('DB_HOST'),
        name = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')
    )
    