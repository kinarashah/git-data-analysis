import psycopg2

def connect_database():
    try:
        conn = psycopg2.connect(dbname='apache-data',user='kshah',host='localhost')
        return conn
    except:
        print "Error connecting to database"

def get_cursor(conn):
    try:
        cursor = conn.cursor()
        return cursor
    except:
        print "Unable to get cursor"

cursor = get_cursor(connect_database())
cursor.execute("select * from applications")
applications = cursor.fetchall()


