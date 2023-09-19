# This module could contain a class that handles all interactions with the SQLite database, such as connecting to the database, executing queries, and closing the connection.

from database. import *

class Status:
    has_stock = False
    quantity = 0
    balance = 0
    avg_price = 0
    min_price = 0
    max_price = 0
    stock_capacity = 12
    capacity = 0
    categories_count = 0
    
    @staticmethod
    def update():
        import os
        if os.path.exists('database/db/stock.db'):
            Status.has_stock = True
            conn = create_connection()
            Status.quantity = sum_quantities(conn)
            Status.balance = get_balance(conn)
            Status.avg_price = get_avg_price(conn)
            Status.min_price = get_min_price(conn)
            Status.max_price = get_max_price(conn)
            Status.capacity = (sum_quantities(conn) / Status.stock_capacity) * 100
            Status.categories_count = get_categories(conn)
        else:
            Status.has_stock = False