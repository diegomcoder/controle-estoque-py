# views/product_view.py and views/category_view.py: These modules could contain functions for displaying products and categories to the user, and for handling user input related to products and categories.
from views.textview import stock_status
from database.status import Status

map_values = {
    "@totquantity": Status.quantity,
    "@totbalance": Status.balance,
    "@avgprice": Status.avg_price,
    "@minprice": Status.min_price,
    "@maxprice": Status.max_price,
    "@maxcapacity": Status.capacity,
    "@level": Status.capacity,
    "@ctgcount": Status.categories_count
}

def replace_keys(text, map_values):
    text2 = text
    for key in map_values:
        print(key, map_values[key])
        text2.replace(key, str(map_values[key]))
    return text2
        
def print_stock_status():
    text = replace_keys(stock_status, map_values)
    print(text)