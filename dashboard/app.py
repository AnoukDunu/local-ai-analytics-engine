import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import streamlit as st
import pandas as pd
from database.connection import get_connection

st.title("Products Analytics Dashboard")

# Establish database connection to fetch data for the dashboard
conn = get_connection()

df = pd.read_sql("SELECT * FROM cln_products", conn)
st.subheader("Products Data")
# st.write() and st.dataframe(df) are both used to display the df. 
# st.write() is more flexible and can display various types of data, while st.dataframe() is specifically designed for displaying DataFrames with additional features like sorting and pagination. 
# You can choose either based on your preference for how you want to display the data.
# st.dataframe(df)
st.write(df)

# Display a bar chart of the top 5 products by estimated revenue
top = df.sort_values(by="estimated_revenue", ascending=False).head(5)
st.subheader("Top 5 Products by Estimated Revenue")
st.bar_chart(top.set_index("title")["estimated_revenue"])

category = df.groupby("category")["estimated_revenue"].sum()
st.subheader("Estimated Revenue by Category")
st.bar_chart(category)
