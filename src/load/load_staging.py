from database.connection import get_connection
import json
from sqlalchemy.dialects.postgresql import JSONB

def load_staging(df):
    conn = get_connection()

    staging_df = df.copy(deep=True)
    staging_df["rating"] = staging_df["rating"].apply(json.dumps)

    dtype_mapping = {
        "rating": JSONB
    }

    staging_df.to_sql('stg_products', con=conn, if_exists='replace', index=False, dtype=dtype_mapping)
    print("Data loaded into staging table successfully.")
    
    if conn is not None:
        conn.close()


# Below is the explanation of the fix for the transformed data not being loaded into the final table:
# The issue was caused by load_staging mutating the original DataFrame before transformation:

# load_staging.py now uses staging_df = df.copy(deep=True) so staging serialization does not alter the source data.
# transform.py keeps a copy of the original DataFrame before processing.
# load_final.py now closes the DB connection in a finally block.
