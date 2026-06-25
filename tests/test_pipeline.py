# Integration testing file for the entire pipeline
from src.extract import extract
from src.transform import transform
# from src.load import lo
from src.database import connection

def test_full_pipeline():
    # Testing extract function first
    api_url = "https://fakestoreapi.com/products"
    df = extract(api_url)

    assert df is not None
    assert len(df) > 0
