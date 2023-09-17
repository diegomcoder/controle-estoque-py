import sqlite3

def get_avg_price(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT SUM (unitary_price) FROM stock")
        prices = cur.fetchone()[0]
        cur.execute("SELECT COUNT (*) FROM stock")
        rows = cur.fetchone()[0]
        return prices / rows
    except sqlite3.Error as e:
        print(e)