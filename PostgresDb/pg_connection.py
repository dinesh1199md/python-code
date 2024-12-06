import psycopg2
import time


def get_db_connection():
    attempt=0
    retry_count=3
    base_sleep=1
    while attempt<retry_count:
        try:
            conn=psycopg2.connect(
                database="postgres",
                user="postgres",
                password="test",
                host="localhost",
                port=5432
            )
            return conn 
        except Exception as e:
            if attempt<retry_count:
                attempt+=1
                print("retry the connection :", attempt)
                base_sleep=base_sleep*2
                time.sleep(base_sleep)
            else:
                print("all retry attempts are fails")
                
try:
    conn= get_db_connection()
    cursor=conn.cursor()
    cursor.execute("select * from cars;")
    data=cursor.fetchall()
    print("data :",data)
except Exception as e:
    print(f"Failed to connect to the database after retries: {e}")
else:
    print("succssfully connection Created")



    