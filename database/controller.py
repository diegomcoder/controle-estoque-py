class Stock:
    capacity = 100
    __conn = None
    
    @staticmethod
    def __create_connection():
        import sqlite3
        try:
            Stock.__conn = sqlite3.connect('database/db/stock.db')
            print(sqlite3.version)
        except sqlite3.Error as e:
            print(e)
        

    def __close_connection():
        Stock.__conn.close()


    def __create_table():
        try:
            cur = Stock.__conn.cursor()
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
    

    def add_product(product):
        try:
            cur = Stock.__conn.cursor()
            cur.execute("INSERT INTO stock (name, category, description, unitary_price, quantity_in_stock) VALUES (?,?,?,?,?)",
                        (product.get_name(),
                        product.get_category(),
                        product.get_description(),
                        product.get_price(),
                        product.get_quantity()))
            Stock.__conn.commit()
            print("Product added")
        except sqlite3.Error as e:
            print(e)


    def exists():
        import os
        return os.path.exists('database/db/stock.db')


    def get_level():
        return (Stock.sum_quantities() / Stock.capacity) * 100


    def get_avg_price():
        try:
            cur = Stock.__conn.cursor()
            cur.execute("SELECT SUM (unitary_price) FROM stock")
            prices = cur.fetchone()[0]
            cur.execute("SELECT COUNT (*) FROM stock")
            rows = cur.fetchone()[0]
            return prices / rows
        except sqlite3.Error as e:
            print(e)


    def get_balance():
        try:
            cur = Stock.__conn.cursor()
            cur.execute("SELECT SUM (unitary_price * quantity_in_stock) FROM stock")
            balance = cur.fetchone()[0]
            return balance
        except sqlite3.Error as e:
            print(e)


    def get_categories():
        try:
            cur = Stock.__conn.cursor()
            cur.execute("SELECT COUNT (DISTINCT category) FROM stock")
            category_count = cur.fetchone()[0]
            return category_count
        except sqlite3.Error as e:
            print(e)


    def get_max_price():
        try:
            cur = Stock.__conn.cursor()
            cur.execute("SELECT MAX (unitary_price) FROM stock")
            max_price = cur.fetchone()[0]
            return max_price
        except sqlite3.Error as e:
            print(e)


    def get_min_price():
        try:
            cur = Stock.__conn.cursor()
            cur.execute("SELECT MIN (unitary_price) FROM stock")
            min_price = cur.fetchone()[0]
            return min_price
        except sqlite3.Error as e:
            print(e)


    def list_products():
        try:
            cur = Stock.__conn.cursor()
            for row in cur.execute('SELECT * FROM stock ORDER BY id'):
                print(row)
        except sqlite3.Error as e:
            print(e)


    def sum_quantities():
        try:
            cur = Stock.__conn.cursor()
            cur.execute("SELECT SUM (quantity_in_stock) FROM stock")
            sum = cur.fetchone()[0]
            return sum
        except sqlite3.Error as e:
            print(e)