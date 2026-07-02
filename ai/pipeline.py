# This file is the brain and it glues everything together. 
# It takes a question, generates a SQL query, executes it, and then explains the results in natural language.
from .sql_generator import generate_sql
from .response_generator import explain_results
from .query_engine import run_query

def ask_database(question):
    # Generate SQL query from the question
    sql = generate_sql(question)
    
    # Execute the SQL query and get results
    data = run_query(sql)
    
    # Explain the results in natural language
    answer = explain_results(question, data)
    
    return sql, data, answer