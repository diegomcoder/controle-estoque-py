import sqlite3

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('database/db/stock.db')
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn