import os
import sys

# --------This was added by CoPilot to resolve an pathing issue affecting the streamlit dashboard!--------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")

for path in (PROJECT_ROOT, SRC_ROOT):
    if path not in sys.path:
        sys.path.insert(0, path)
# --------End of CoPilot addition--------

import streamlit as st
import pandas as pd
from database.connection import get_connection
from ai.pipeline import ask_database
# # The above pathing was changed to resolve an issue affecting the streamlit dashboard!
from src.main import run_pipeline  # Import the run_pipeline function from main.py
st.title("Products Analytics Dashboard")

if st.button("Run Data Pipeline", on_click=run_pipeline):
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

    # This is the newly added AI interface for asking questions about the data. 
    # It uses the ask_database function from the ai.pipeline module to generate SQL queries, execute them, and explain the results in natural language.
st.title("AI Interface for Data Queries")

# input field for the user to type questions.
user_question = st.text_input("Type your question, fool:")

# Creating a button to trigger the AI query
if st.button("Run Query!"):
    if user_question:
        st.spinner("Processing your question...")
        try:
            sql, data, answer = ask_database(user_question)
            
            with st.expander("See full details"):
                st.subheader("Generated SQL Query")
                st.code(sql, language="sql")
            
                st.subheader("Raw Data")
                st.write(data)

            st.subheader("AI Answer:")
            st.success(answer)
        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question first, dumbo!")