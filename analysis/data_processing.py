import pandas as pd
from datetime import datetime

def process_books(data):
    df=pd.DataFrame(data)
    
    df["price"]=df["price"].str.replace("£", "")
    df["price"]=df["price"].astype(float)

    return df

def generate_report(df):
    df["data_collection"]=datetime.now().strftime("%Y-%m-%d %H:%M")

    df=df.rename(columns={
        "title": "product",
        "price": "price",
        "link": "link"
    })

    df=df.sort_values(by="price", ascending=False)
    df["price"]=df["price"].apply(lambda x: f"R$ {x:.2f}")
    df.to_csv("report.csv", index=False, encoding="utf-8-sig")

    print("Professional report generated: report.csv")