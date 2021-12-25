import psycopg2

def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="imdbload", user="postgres", password="postgres")

        cur = conn.cursor()
        cur.execute("SELECT * from movieinfo")
        
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
        print(row)
        print('xxx')
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:

        if conn is not None:
            print('xx')
            conn.close()

get_vendors()