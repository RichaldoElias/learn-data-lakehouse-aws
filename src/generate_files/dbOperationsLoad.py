import sqlite3

# Paths
sqlite_db = "src/db/classicmodels.db"
mysql_sql_file = "src/db/mysqlsampledatabase.sql"

# Read MySQL script
with open(mysql_sql_file, "r", encoding="utf-8") as f:
    sql_script = f.read()

# Format the statements to be executed and compatibility fixes
statements = sql_script.split(";\n")
statements_to_execute = [sts.strip() + ";" for sts in statements if sts.strip()]

# Connect to SQLite using a context manager to avoid locking
with sqlite3.connect(sqlite_db) as conn:
    cursor = conn.cursor()

    for statement in statements_to_execute:
        try:
            cursor.execute(statement.replace(";;", ";"))
        except Exception as e:
            print(f"Skipped statement: {statement[:80]}...\n   Error: {e}")

    conn.commit()
