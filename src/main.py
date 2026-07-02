# This is the main entry point for the application. It initializes the application and starts the main loop.
# The pipeline orchestration is also handled here, ensuring that all components are properly initialized and executed in the correct order.
from extract.extract import extract
from load.load_staging import load_staging
from transform.transform import transform_data
from load.load_final import load_final
from utilities.logger import get_logger
from utilities.quality_checks import run_all_checks
# adding the AI pipeline to the main.py file
# from ai.pipeline import ask_database

logger = get_logger(__name__)
# function that runs the entire pipeline: extract, transform, load, and quality checks
def run_pipeline():
    logger.info("Starting the data pipeline...")

    # Extract data from API
    api_url = "https://fakestoreapi.com/products"
    df = extract(api_url)
    

    # testing connection to database
    # connection = get_connection()

    if df is not None:
        logger.info("Data extraction successful, proceeding with transformation and loading...")
        # Load data into staging table
        load_staging(df)
        # transforming data
        cleaned_df = transform_data(df)
        # run quality checks on the cleaned data
        run_all_checks(cleaned_df)
        # load cleaned and transformed data into the final table
        load_final(cleaned_df)
        logger.info("Data pipeline completed successfully.")
        return True
    else:
        logger.error("Data extraction failed.")
        return False



if __name__ == "__main__":
    run_pipeline()
