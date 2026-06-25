from database.connection import engine
import pandas as pd
from utilities.logger import get_logger

# Initialize logger for this module
logger = get_logger(__name__)

def load_final(df):
    logger.info("Starting to load data into the final table...")
    # use an engine-managed transaction so commits happen automatically
    try:
        with engine.begin() as conn:
            existing = pd.read_sql("SELECT id FROM cln_products", conn)

            df_to_load = df[~df['id'].isin(existing['id'])]

            if df_to_load.empty:
                logger.info("No new unique records to load into final table.")
                return

            df_to_load.to_sql('cln_products', conn, if_exists='append', index=False)
            logger.info("Data loaded into final table successfully.")
    except Exception as e:
        logger.error(f"An error occurred while loading data into the final table: {e}")
    