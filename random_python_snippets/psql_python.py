import psycopg2
import sys

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE mytable2 (id serial PRIMARY KEY, \"user\" text NOT NULL, age integer NOT NULL);")

conn.commit()
cursor.close()
conn.close()
