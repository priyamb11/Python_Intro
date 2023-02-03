import sqlite3
import pandas as pd

conn = sqlite3.connect("employee.db")

data = pd.read_csv("Coding Stuff/sql.csv")

query1 = pd.read_sql("""
        SELECT *
        FROM EMP
""",
conn)

query2 = pd.read_sql("""
        SELECT JOB, SUM(SAL)
        FROM EMP
        GROUP BY JOB
""",
conn)

print(query2)