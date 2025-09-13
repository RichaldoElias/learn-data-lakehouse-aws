"""
Exports all tables from a SQLite database to individual CSV files.

This script connects to a SQLite database located at 'assets/db/classicmodels.db',
retrieves all user-defined tables, and exports each table's contents to a separate
CSV file inside the 'assets/db/csv_exports' directory. The CSV files are named after
their corresponding table names.

Dependencies:
- sqlite3 (standard library)
- pandas
- os (standard library)

Usage:
    Run this script directly to generate CSV exports of all tables in the database.

Example:
    > python export_sqlite_to_csv.py
    ✅ Exported customers to assets/db/csv_exports/customers.csv
    ✅ Exported orders to assets/db/csv_exports/orders.csv
    ...
"""


import os
import sqlite3
import pandas as pd

DB_PATH = "assets/db/classicmodels.db"
OUTPUT_DIR = "assets/db/csv_exports"

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    csv_path = os.path.join(OUTPUT_DIR, f"{table}.csv")
    df.to_csv(csv_path, index=False)
    print(f"✅ Exported {table} to {csv_path}")

conn.close()
