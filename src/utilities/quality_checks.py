# file to do DataFrame quality checks
from utilities.logger import get_logger
# Calling the logger here too, to check if the logic works (which it rarely does)
logger = get_logger(__name__)

def check_empty(df):
    if df.empty:
        logger.warning("The DataFrame is empty.")
        raise ValueError("The DataFrame is empty.")
    return True

def check_nulls(df):
    if df.isnull().values.any():
        logger.warning("The DataFrame contains null values.")
        raise ValueError("The DataFrame contains null values.")
    return True

def check_duplicates(df):
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        logger.warning(f"The DataFrame contains {duplicate_count} duplicate rows.")
        raise ValueError(f"The DataFrame contains {duplicate_count} duplicate rows.")
    return True

def run_all_checks(df):
    logger.info("Started running quality checks on the DataFrame...")
    check_empty(df)
    check_nulls(df)
    check_duplicates(df)
    logger.info("All quality checks passed successfully.")
    return True