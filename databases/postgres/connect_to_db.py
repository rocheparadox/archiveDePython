#powered by rocheparadox
#make sure psql server is running in the specified port and the user has enough permission to connect the specified database

import psycopg2

host = 'localhost'
port = '5432'
database = 'postgres'
user = 'postgres'

conn = None

try:
    conn = psycopg2.connect(host=host, port=port, database=database, user=user, password='postgres')
    cur = conn.cursor()
    cur.execute('select * from User')
    db_users = cur.fetchone()
    print(db_users)
    cur.close()
except Exception as exc :
    print('---Error occured while trying to connect to the database --- ' + str(exc))

finally:
    if conn != None:
        conn.close()
