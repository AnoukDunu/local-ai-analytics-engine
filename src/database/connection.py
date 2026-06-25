from config.config import get_engine

# creates a single engine instance that can be imported and used across the application
# AKA a global instance
engine = get_engine()

def get_connection():

    try:
        connection = engine.connect()
        print("Database connection established successfully.")
        return connection
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None
    # finally:
    #     print("Closing database connection.")
    #     connection.close()