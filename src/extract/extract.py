import requests
import pandas as pd
from utilities.logger import get_logger

# Initialize logger for this module
logger = get_logger(__name__)

def extract(api_url):
    url = api_url

    try:
        logger.info("Starting data extraction...")
        response = requests.get(url)

        # added the below line to auto-raise an error if the HTTP request returned an unsuccessful status code (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data)

        # The below line is added to simulate real-world issues like duplicate data or messy data. To add depth to the data and projhect.
        # please hire me :(
        df = pd.concat([df, df.iloc[:3]])

        logger.info("Data extraction successful!")
        return df

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while making the API request: {e}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred while parsing API response: {e}")
        return None