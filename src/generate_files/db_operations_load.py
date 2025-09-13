"""
Executes a MySQL-format SQL script on a SQLite database.

This script reads a SQL dump file originally formatted for MySQL (e.g., 
'assets/db/mysqlsampledatabase.sql'), splits it into individual SQL statements,
and executes them sequentially on a SQLite database located at 
'assets/db/classicmodels.db'.

To ensure compatibility and avoid database locking:
- Statements are split on ';\n'
- Empty or malformed statements are skipped
- The database connection is managed using a context manager

Note:
- The script assumes the SQL syntax is mostly compatible with SQLite.
- Some MySQL-specific features may need to be manually edited in the script.

Usage:
    Run this script after creating or resetting the SQLite database to populate it 
    with schema and data from the MySQL sample.

Example:
    > python import_mysql_to_sqlite.py
    Skipped statement: CREATE TABLE orders ( ... ) ...
       Error: near "AUTO_INCREMENT": syntax error
"""


import sqlite3

# Paths
SQLITE_DB = "assets/db/classicmodels.db"
MYSQL_SQL_FILE = "assets/db/mysqlsampledatabase.sql"

# Read MySQL script
with open(MYSQL_SQL_FILE, "r", encoding="utf-8") as f:
    sql_script = f.read()

# Format the statements to be executed and compatibility fixes
statements = sql_script.split(";\n")
statements_to_execute = [sts.strip() + ";" for sts in statements if sts.strip()]

# Connect to SQLite using a context manager to avoid locking
with sqlite3.connect(SQLITE_DB) as conn:
    cursor = conn.cursor()

    for statement in statements_to_execute:
        try:
            cursor.execute(statement.replace(";;", ";"))
        except Exception as e:
            print(f"Skipped statement: {statement[:80]}...\n   Error: {e}")

    conn.commit()
