class DataBase:
    import sqlite3
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE stock(name, description, unitary price, amount)")