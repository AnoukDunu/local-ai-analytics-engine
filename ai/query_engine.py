# This file is what wil run SQL
from db import get_connection

def run_query(sql):
    # start the database connection
    conn = get_connection()
    # create a cursor to be able to execute sql queries in the database
    cursor = conn.cursor()
    # pass the SQL query to be executed
    cursor.execute(sql)
    # retrive results and store in the 'results'
    results = cursor.fetchall()
    # close database connection
    conn.close()
    # return results
    return results