from methods import exit_program
from methods import get_user_command
from methods import load_demo_stock
from methods import update_stock_status
from methods import prompt_user_for_data
from methods import print_menu
from modules import *

import json
with open('./data/msg.json', encoding="utf-8") as my_json:
    msg = json.load(my_json)

stock = {}
lang = "pt"
msg = msg[lang]

print(msg)

# PERFORM GRAPHICS
os.system("cls")
print(msg["welcome"])
print_menu(msg["start_empty_stock"], msg["load_demo_stock"], msg["exit_stock_control"])

input_text = prompt_user_for_data("^[1-3]$", msg["enter_command"])
input_number = int(input_text)

if input_number == 3:
    exit_program()
elif input_number == 2:
    stock = load_demo_stock()
    update_stock_status(stock)
else:
    update_stock_status(stock)