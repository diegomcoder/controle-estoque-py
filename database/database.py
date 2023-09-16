# This module could contain a class that handles all interactions with the SQLite database, such as connecting to the database, executing queries, and closing the connection.

def db_init():
    import sqlite3
    import os
    
    db_path = 'stock.db'
    
    if not os.path.exists(db_path):
        connection = sqlite3.connect("stock.db")
        
        cursor = connection.cursor()
        
        # cursor.execute("CREATE TABLE products(name, description, price, amount)")
        cursor.execute('''
        CREATE TABLE produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            unitary_price REAL NOT NULL,
            quantity_in_stock INTEGER NOT NULL
        )
        ''')

        # Confirme as alterações e feche a conexão
        connection.commit()
        print('Database created successfully')
        connection.close()
    else:
            print('Database already exists')