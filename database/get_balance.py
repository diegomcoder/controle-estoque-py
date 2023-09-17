import sqlite3

def get_balance(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT SUM (unitary_price * quantity_in_stock) FROM stock")
        balance = cur.fetchone()[0]
        return balance
    except sqlite3.Error as e:
        print(e)