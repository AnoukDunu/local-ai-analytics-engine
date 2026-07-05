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

# Creating a function to create charts from AI query outputs
def generate_chart(data):
    # converting data to a DataFrame
    df = pd.DataFrame(data)

    if df.empty:
        st.warning("No data returned from the query.")
        return
    
    st.write("Query Result DataFrame:")

    # detecing if dataframe has numeric columns for charting
    numeric_cols = df.select_dtypes(include=['number']).columns

    # detecting if dataframe has categorical columns for charting
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Bar chart scenario: if 1 numeric + 1 category
    if len(numeric_cols) >= 1 and len(categorical_cols) >= 1:
        x_col = categorical_cols[0]
        y_col = numeric_cols[0]

        chart_data = df.set_index(x_col)[y_col]
        st.bar_chart(chart_data)
    elif len(numeric_cols) >= 1:
        # Line chart scenario: if only numeric columns are present
        st.line_chart(df[numeric_cols])
    else:
        st.warning("The returned data does not have numeric columns for charting.")


st.set_page_config(page_title="Products Analytics Dashboard", layout="wide")
st.title("Products Analytics Dashboard")

# ==================================================
# Initialise session state for pipeline results
if "products_df" not in st.session_state:
    st.session_state["products_df"] = None

# Initialising the session state for the AI chat history
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

# Initialise session state to store the LLM thinking process per query
if "thinking_process" not in st.session_state:
    st.session_state["thinking_process"] = []
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

# ====================================== AI interface ======================================
st.sidebar.title("QueryMind AI")

# Displaying the chat history in the sidebar
for message in st.session_state["chat_messages"]:
    with st.sidebar.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("role") == "assistant" and message.get("thinking"):
            with st.expander("View thinking"):
                st.subheader("Generated SQL Query")
                st.code(message["thinking"]["sql"], language="sql")

                st.subheader("Raw Data")
                st.write(message["thinking"]["data"])

# Chat input for the user
user_input = st.sidebar.chat_input("Talk to me...")

# When a user submits a message/question
if user_input:
    # Store the user's messsage in the chat history
    st.session_state["chat_messages"].append({
        "role": "user",
        "content": user_input
    })

    # Display the user message in the sidebar
    with st.sidebar.chat_message("user"):
        st.markdown(user_input)


    try:
        # Copilot added this to make tge spinner appear in the sidebar instead of the main page.
        spinner_placeholder = st.sidebar.empty() 
        with spinner_placeholder.container():
            with st.spinner("Thinking..."):
                sql, data, answer = ask_database(user_input)

        assistant_reply = answer
        
        thinking_entry = {
            "query": user_input,
            "sql": sql,
            "data": data,
            "answer": answer,
        }

        # Save the assistant's response
        st.session_state["chat_messages"].append({
            "role": "assistant",
            "content": assistant_reply,
            "thinking": thinking_entry,
        })

        # Save the thinking process results in the session state
        st.session_state["thinking_process"].append(thinking_entry)

        # Display the assistant's response
        with st.sidebar.chat_message("assistant"):
            st.markdown(assistant_reply)

            # Autogenerated chart
            generate_chart(data)

            # Expander to show thinking process if user requires it
            with st.expander("View thinking"):
                st.subheader("Generated SQL Query")
                st.code(sql, language="sql")

                st.subheader("Raw Data")
                st.write(data)

    except Exception as e:
        st.sidebar.error(f"Error: {e}")