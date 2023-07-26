from modules import *

# LOADS A DEMONSTRATIVE STOCK THAT'S STORED ON AN EXTERNAL JSON FILE
def load_demo_stock():
    import json
    with open("./data/demo_stock.json", encoding='utf-8') as my_json:
        return json.load(my_json)

    