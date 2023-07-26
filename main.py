from methods import exit_program
from methods import get_user_command
from methods import load_demo_stock
from methods import update_stock_status
import os

stock = {}

def main():
    # CALL THE START OF THE PROGRAM
    os.system("cls")
    print("🔴 BEM VINDO!\n")
    print("(1) Iniciar com estoque vazio")
    print("(2) Carregar estoque demonstrativo")
    print("(3) Fechar o controle de estoque")

    amountOfOptions = 3
    userCommand = get_user_command(amountOfOptions)
    global stock

    if userCommand == "3":
        exit_program()
    elif userCommand == "2":
        # global stock
        stock = load_demo_stock()
        # os.system("cls")
        # print("ESTOQUE DEMONSTRATIVO CARREGADO!")
        update_stock_status(stock)
    else:
        update_stock_status(stock)

main()