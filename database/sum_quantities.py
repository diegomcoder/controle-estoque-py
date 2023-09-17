import sqlite3

def sum_quantities(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT SUM (quantity_in_stock) FROM stock")
        sum = cur.fetchone()[0]
        return sum
    except sqlite3.Error as e:
        print(e)