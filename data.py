import pandas as pd
import sqlite3


con = sqlite3.connect("messages.db")
df = pd.read_sql_query("SELECT * from Form_Response", con)


cursor = con.cursor()

cursor.execute("SELECT * from Form_Response")

rows = cursor.fetchall()
for row in rows:
    print(row)



con.close()