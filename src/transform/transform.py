from utilities.logger import get_logger

logger = get_logger(__name__)

def transform_data(df):

    logger.info("Starting data transformation...")
    
    df = df.copy()
    df = df[['id', 'title', 'price', 'description', 'category', 'image', 'rating']]

    # Extracting the nested JSON in 'rating' column into separate columns
    df['rating_rate'] = df['rating'].apply(lambda x: x.get('rate') if isinstance(x, dict) else None)
    df['rating_count'] = df['rating'].apply(lambda x: x.get('count') if isinstance(x, dict) else None)

    # Drop the original 'rating' column as it's no longer needed
    df = df.drop(columns=['rating'])

    logger.info("Performing quality checks...")
    df = df.dropna()
    df = df[df['price'] > 0]  #Remove products with non-positive prices

    # removing duplicates if any
    df = df.drop_duplicates(subset=['id'])

    # estimating the revenue using the current price and number of reviews
    df['estimated_revenue'] = df['price'] * df['rating_count']

    logger.info("Data transformation completed successfully.")
    return df