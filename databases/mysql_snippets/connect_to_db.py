import mysql.connector

user='test'
password='test'
host='roche-6660'
port=46000
database = 'literature'
conn = None

try:
    conn = mysql.connector.connect(user=user, password=password, port=port, host=host, database=database)

    if conn.is_connected():
        print('successfully connected to the database' + database)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (author_name, born_year, death_year, era) values ("John Milton", 1608, 1674, "AD")')
        conn.commit()
        cursor.close()
    else:
        print('There was a problem in connecting to the database')

except Exception as exception:
    print("Follwing error occured while trying to connect to the database" + str(exception))

finally:
    if conn != None:
        conn.close()