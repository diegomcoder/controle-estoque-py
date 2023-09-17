import sqlite3

def list_products(conn):
    try:
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM stock ORDER BY id'):
            print(row)
    except sqlite3.Error as e:
        print(e)