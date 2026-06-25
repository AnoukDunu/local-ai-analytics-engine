import logging
import os

# Creating a logs directory in the project root if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Preventing duplicate logs by checking if handlers already exist
    if not logger.handlers:
        # Create a file handler that logs to a file named 'pipeline.log' in the logs directory
        file_handler = logging.FileHandler('logs/pipeline.log')

        # Create a console handler that logs to the console
        console_handler = logging.StreamHandler()

        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger