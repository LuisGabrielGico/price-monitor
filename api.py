from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
from config import DB_URL

app=FastAPI(
    title="Price Monitor API",
    description="API for monitoring prices of products collected automatically",
    version="1.0.0"
)

engine=create_engine(DB_URL)

@app.get("/")
def home():
    return{"message": "Price monitoring API"}

@app.get("/products", summary="List all the products")
def get_products():
    df=pd.read_sql("SELECT * FROM books", engine)

    return {
        "total": len(df),
        "data": df.to_dict(orient="records")
    }

@app.get("/products/filter", summary="Filter products by price")
def filter_products(max_price: float):
    query="SELECT * FROM books WHERE price <= %s"
    df=pd.read_sql(query, engine, params=(max_price,))
    
    return {
        "total": len(df),
        "data": df.to_dict(orient="records")
    }