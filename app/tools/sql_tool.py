import sqlite3
import pandas as pd

DB_PATH = "app/database/ventas.db"

def execute_sql(query: str):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df
