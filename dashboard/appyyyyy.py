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

if "pipeline_run" not in st.session_state:
    st.session_state.pipeline_run = False
if "query_result" not in st.session_state:
    st.session_state.query_result = None
if "query_error" not in st.session_state:
    st.session_state.query_error = None

if st.button("Run Data Pipeline"):
    st.session_state.pipeline_run = True

if st.session_state.pipeline_run:
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM cln_products", conn)

    st.subheader("Products Data")
    st.write(df)

    top = df.sort_values(by="estimated_revenue", ascending=False).head(5)
    st.subheader("Top 5 Products by Estimated Revenue")
    st.bar_chart(top.set_index("title")["estimated_revenue"])

    category = df.groupby("category")["estimated_revenue"].sum()
    st.subheader("Estimated Revenue by Category")
    st.bar_chart(category)

st.header("AI Interface for Data Queries")

with st.form("query_form"):
    user_question = st.text_input("Type your question", key="user_question")
    submitted = st.form_submit_button("Run Query")

if submitted:
    if user_question:
        st.session_state.query_error = None
        st.session_state.query_result = None
        with st.spinner("Processing your question..."):
            try:
                sql, data, answer = ask_database(user_question)
                st.session_state.query_result = {
                    "sql": sql,
                    "data": data,
                    "answer": answer,
                }
            except Exception as exc:
                st.session_state.query_error = str(exc)
    else:
        st.session_state.query_error = "Please enter a question first."

if st.session_state.query_error:
    st.warning(st.session_state.query_error)

if st.session_state.query_result is not None:
    result = st.session_state.query_result
    with st.expander("See full details"):
        st.subheader("Generated SQL Query")
        st.code(result["sql"], language="sql")

        st.subheader("Raw Data")
        st.write(result["data"])

    st.subheader("AI Answer")
    st.success(result["answer"])
