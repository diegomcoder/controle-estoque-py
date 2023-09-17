import sqlite3

def get_categories(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT (DISTINCT category) FROM stock")
        category_count = cur.fetchone()[0]
        return category_count
    except sqlite3.Error as e:
        print(e)