import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from config import DB_URL

st.title("📊 Price Monitoring Dashboard")

engine=create_engine(DB_URL)

df=pd.read_sql("SELECT * FROM books", engine)

st.subheader("📋 Data Table")
st.dataframe(df)

st.subheader("📈 Price Distribution")
st.bar_chart(df["price"])

max_price=st.slider("Maximum price", 0.0, float(df["price"].max()))
filtered_df=df[df["price"] <= max_price]
st.dataframe(filtered_df)