import pandas as pd
import sqlite3
import psycopg2
import psycopg2.extras


con = psycopg2.connect("postgresql://contact_query_databse_user:SYWt3zrIo3aEjJDqwcxemqaz6HuMMmkU@dpg-ch5l8s5269v5rfrcrp50-a.oregon-postgres.render.com/contact_query_databse")
df = pd.read_sql_query("SELECT * from Form_Response", con)


cursor = con.cursor()

cursor.execute("SELECT * from Form_Response")

rows = cursor.fetchall()
for row in rows:
    print(row)



con.close()