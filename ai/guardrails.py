# This file has the guardrails so that the LLM doesn't alter tables in any way.
import re

def is_query_safe(query:str)-> bool:
    # Checks if query is safe to run against the database. Returns True if safe, False otherwise.
    if not query:
        return False
    
    # Convert the query to lowercase for case-insensitive matching
    query_lower = query.lower()

    # Create a dictionary of forbidden keywords and their corresponding regex patterns
    forbidden_keywords = {
        "delete",
        "update",
        "insert",
        "drop",
        "alter",
        "truncate",
        "create"
    }

    # forbidden_keywords = {
    #     "delete": r"\bdelete\b",
    #     "update": r"\bupdate\b",
    #     "insert": r"\binsert\b",
    #     "drop": r"\bdrop\b",
    #     "alter": r"\balter\b",
    #     "truncate": r"\btruncate\b",
    #     "create": r"\bcreate\b",
    # }

    for keyword in forbidden_keywords:
        if keyword in query_lower:
            return False
        
    # Only allow SELECT statements and basic clauses like WHERE, GROUP BY, ORDER BY, etc.
    if not query_lower.strip().startswith("select"):
        return False
    
    # Checking if correct table is used
    allowed_tables = {"cln_products"}

    # Matching table name
    # The regex pattern was taken straight from AI because I don't fully understand regex patterns.
    table_match = re.findall(r"from\s+(\w+)", query_lower)

    if table_match:
        for table in table_match:
            if table not in allowed_tables:
                return False
            
    return True