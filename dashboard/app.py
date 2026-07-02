import os
import sys

# --------This was added by CoPilot to resolve a pathing issue affecting the Streamlit dashboard!--------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")

for path in (PROJECT_ROOT, SRC_ROOT):
    if path not in sys.path:
        sys.path.insert(0, path)
# --------End of CoPilot addition--------

import pandas as pd
import streamlit as st
from ai.pipeline import ask_database
from database.connection import get_connection
from src.main import run_pipeline

st.set_page_config(page_title="Products Analytics Dashboard", layout="wide")
st.title("Products Analytics Dashboard")

# ==================================================
# Initialise session state for pipeline results
if "products_df" not in st.session_state:
    st.session_state["products_df"] = None

# Initialise the session state for AI query results
if "ai_results" not in st.session_state:
    st.session_state["ai_results"] = None
# ==================================================

# Triggering the Pipeline Run Button
if st.button("Run Data Pipeline", on_click=run_pipeline):
    conn = get_connection()
    st.session_state["products_df"] = pd.read_sql("SELECT * FROM cln_products", conn)

# Displaying the Products Data and Visualizations on the dashboard
if st.session_state["products_df"] is not None:
    df = st.session_state["products_df"]
    
    st.subheader("Products Data")
    st.write(df)

    top = df.sort_values(by="estimated_revenue", ascending=False).head(5)
    st.subheader("Top 5 Products by Estimated Revenue")
    st.bar_chart(top.set_index("title")["estimated_revenue"])

    category = df.groupby("category")["estimated_revenue"].sum()
    st.subheader("Estimated Revenue by Category")
    st.bar_chart(category)

# AI interface
st.title("AI Interface for Data Queries")

with st.form("query_form"):
    user_question = st.text_input("Type your question, fool:")
    submitted = st.form_submit_button("Run Query!")

# Triggering the AI querry button
if submitted:
    if user_question:
        with st.spinner("Processing your question..."):
            try:
                sql, data, answer = ask_database(user_question)
                # Store all three pieces of data as a dictionary inside session state
                st.session_state["ai_results"] = {
                    "sql": sql,
                    "data": data,
                    "answer": answer
                }
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first, dumbo!")
        st.session_state["ai_results"] = None

# Displaying the AI query results on the dashboard
if st.session_state["ai_results"] is not None:
    results = st.session_state["ai_results"]
    
    with st.expander("See full details"):
        st.subheader("Generated SQL Query")
        st.code(results["sql"], language="sql")
    
        st.subheader("Raw Data")
        st.write(results["data"])

    st.subheader("AI Answer:")
    st.success(results["answer"])