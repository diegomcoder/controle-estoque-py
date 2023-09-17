from database import add_product, get_products
from views import display_products, ask_for_product

def add_new_product():
    product = ask_for_product()
    add_product(product)

def show_products():
    products = get_products()
    display_products(products)