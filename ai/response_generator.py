# This file is to make the results more human-readable (in natural language basically)
from .llm import ask_llm
# The above pathing was changed to resolve an issue affecting the streamlit dashboard!
def explain_results(question, data):
    prompt = f"""
    You are a data analyst. You will be given a question and the results of a SQL query. 
    Your task is to explain the results in natural language, providing insights and context based on the data.

    Question: {question}
    Data: {data}

    Only return the explanation. Do not include any SQL queries or additional text.
    Explain the answer clearly.
    """

    return ask_llm(prompt)