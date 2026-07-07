# This file is the brain and it glues everything together. 
# It takes a question, generates a SQL query, executes it, and then explains the results in natural language.
from .sql_generator import generate_sql
from .response_generator import explain_results
from .query_engine import run_query
from .guardrails import is_query_safe
# Copilot change the above pathing to resolve an issue affecting the streamlit dashboard!

def ask_database(question):
    # Generate SQL query from the question
    sql = generate_sql(question)

    # Implementing guardrails to ensure the SQL query is safe before executing it
    if not is_query_safe(sql):
        raise ValueError("Unsafe query generated. Request denied!")
    
    # Execute the SQL query and get results
    data = run_query(sql)
    
    # Explain the results in natural language
    answer = explain_results(question, data)
    
    return sql, data, answer