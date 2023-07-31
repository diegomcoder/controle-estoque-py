from methods import exit_program
from methods import get_user_command
from methods import load_demo_stock
from methods import update_stock_status
from modules import *

stock = {}

os.system("cls")

print("🔴 BEM VINDO!\n")
print("(1) Iniciar com estoque vazio")
print("(2) Carregar estoque demonstrativo")
print("(3) Fechar o controle de estoque")

amount_of_options = 3
user_input = get_user_command(amount_of_options)

if user_input == 3:
    exit_program()
elif user_input == 2:
    stock = load_demo_stock()
    update_stock_status(stock)
else:
    update_stock_status(stock)

