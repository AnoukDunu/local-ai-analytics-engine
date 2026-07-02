# The below pathing was changed to resolve an issue affecting the streamlit dashboard!
from .llm import ask_llm
from .schema import get_schema

# This code will prompt the LLM to generate a SQL query based on the provided question and database schema. 
# It uses the `ask_llm` function to send the prompt to the local LLM and retrieve the generated SQL query. 
# The `get_schema` function is used to obtain the database schema that will be included in the prompt.
def generate_sql(question):
    schema = get_schema()

    prompt = f"""
    You are a PostgreSQL expert. You will be given a question and a database schema. 
    Your task is to convert a question into a valid SQL query that can be executed against the provided schema.

    {schema}

    Question: {question}

    Only return SQL query. Do not include any explanations or additional text.
    """

    return ask_llm(prompt)