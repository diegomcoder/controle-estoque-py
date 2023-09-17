import sqlite3

def get_min_price(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT MIN (unitary_price) FROM stock")
        min_price = cur.fetchone()[0]
        return min_price
    except sqlite3.Error as e:
        print(e)