
import psycopg2,pandas

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="YourUsername",
    password="YourPassword"
)

cursor=conn.cursor()
cursor.execute("sql")
out=cursor.fetchall()
# conn.commit() #commite the changes 
cursor.close()

file=pandas.DataFrame(out).to_csv("csv_file")


import psycopg2
try:
    conn=psycopg2.connection(host="",databasename="",username="",password="",posrt=5432)
    cur=conn.cursor()
    cur.execute("selecte * from table;")
    data=cur.featchall()
except Exception as e:
    print("error in the connection:",e)
else:
    print("conection created and executed the query") 
finally:
    cur.close()
    conn.close()
    print("Database connection closed!!")

    