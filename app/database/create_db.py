import sqlite3
import pandas as pd

df = pd.read_csv("app/database/ventas.csv")

conn = sqlite3.connect("app/database/ventas.db")

df.to_sql("ventas", conn, if_exists="replace", index=False)

print("Base de datos creada correctamente")
