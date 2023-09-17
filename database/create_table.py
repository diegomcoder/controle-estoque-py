import sqlite3

def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute('''
        CREATE TABLE stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            unitary_price REAL NOT NULL,
            quantity_in_stock INTEGER NOT NULL
        )
        ''')
        print("Table created")
    except sqlite3.Error as e:
        print(e)