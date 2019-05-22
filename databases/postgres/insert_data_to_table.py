#powered by rocheparadox
#make sure psql server is running in the specified port and the user has enough permission to connect the specified database

import psycopg2

host = 'localhost'
port = '12000'
database = 'jack'
user = 'postgres'

conn = None
x=open('/home/local/ZOHOCORP/roche-6660/witch.txt').read()
try:
    conn = psycopg2.connect(host=host, port=port, database=database, user=user, password='postgres')
    cur = conn.cursor()
    #cur.execute('select * from queen')
    cur.execute('insert into queen(title,pro) values(\''+x[1:60000]+'\',\'broom\')')
    #db_users = cur.fetchone()
    #print(db_users)
    conn.commit()
    cur.close()
except Exception as exc :
    print('---Error occured while trying to connect to the database --- ' + str(exc))

finally:
    if conn != None:
        conn.close()