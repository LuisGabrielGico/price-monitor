from sqlalchemy import create_engine
from config import DB_URL

engine=create_engine(DB_URL)

def save_books(df):
    try:
        df.to_sql(
            "books",
            engine,
            if_exists="append",
            index=False
        )
    except Exception as e:
        print("Duplicate detected, ignore...")