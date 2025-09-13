import sqlite3
import pandas as pd
import os

db_path = "src/db/classicmodels.db"
output_dir = "src/db/csv_exports"

os.makedirs(output_dir, exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    csv_path = os.path.join(output_dir, f"{table}.csv")
    df.to_csv(csv_path, index=False)
    print(f"✅ Exported {table} to {csv_path}")

conn.close()
