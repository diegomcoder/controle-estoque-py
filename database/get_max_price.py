import sqlite3

def get_max_price(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT MAX (unitary_price) FROM stock")
        max_price = cur.fetchone()[0]
        return max_price
    except sqlite3.Error as e:
        print(e)