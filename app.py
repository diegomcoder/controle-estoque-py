# app.py: This is the main entry point of your application. It could set up the database and handle the main loop of your application, asking for user input and responding to it.

from models.product import Product
from database.controller import Stock

def get_user_command(regex):
    import re
    return re.search(regex, input())

def main():
    products = [
        Product("Smart TV 32'", "Vídeo", "Smart TV Samsung 32 pol com Android ...", 1299.89, 12),
        Product("Samsung Galaxy A14", "Smartphones", "Smartphone Samsung Galaxy A14 120GB ...", 989.55, 34),
        Product("Air frier", "Cozinha", "Fritadeira sem oleo air frier ...", 340.82, 13),
        Product("Lenovo Ideapad 32A", "Notebooks", "Notebook Lenovo Intel Core i5 480GB SSD ...", 3262.12, 6)
    ]

    if not Stock.exists():
        Stock.__create_connection()
        Stock.__create_table()

        for product in products:
            Stock.add_product(product)
        print(Stock.list_products())
        Stock.__close_connection()
    
    #print_stock_status()

    #opt = get_user_command('^[1-3]$')
    #print(opt)


main()