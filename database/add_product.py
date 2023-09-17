import sqlite3


def add_product(conn, product):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO stock (name, category, description, unitary_price, quantity_in_stock) VALUES (?,?,?,?,?)",
                    (product.get_name(),
                    product.get_category(),
                    product.get_description(),
                    product.get_price(),
                    product.get_quantity()))
        conn.commit()
        print("Product added")
    except sqlite3.Error as e:
        print(e)
