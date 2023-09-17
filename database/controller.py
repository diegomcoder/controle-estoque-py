from database import create_connection, create_table, add_product, list_products, close_connection
from models.product import Product

products = [
    Product("Smart TV 32'", "Vídeo", "Smart TV Samsung 32 pol com Android ...", 1299.89, 12),
    Product("Samsung Galaxy A14", "Smartphones", "Smartphone Samsung Galaxy A14 120GB ...", 989.55, 34),
    Product("Air frier", "Cozinha", "Fritadeira sem oleo air frier ...", 340.82, 13),
    Product("Lenovo Ideapad 32A", "Notebooks", "Notebook Lenovo Intel Core i5 480GB SSD ...", 3262.12, 6)
]

def implement_db():
    conn = create_connection()
    create_table(conn)
    for product in products:
        add_product(conn, product)
    list_products(conn)
    close_connection(conn)