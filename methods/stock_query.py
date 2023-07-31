import methods
from modules import *

# STOCK QUERY
def stock_query(stock):
    print("\n\n\n")
    os.system("cls")
    print("🔴 CONSULTA DE ESTOQUE")
    print("\n\nO que deseja fazer?\n")
    print("(1) Listar produtos de uma categoria")
    print("(2) Listar produtos segundo o preço")
    print("(3) Voltar ao inventário de estoque")
    print("(4) Fechar o controle de estoque")

    options_amount = 4
    chosen_command = methods.get_user_command(options_amount)

    if chosen_command == 4:
        methods.exit_program()
        return
    elif chosen_command == 3:
        methods.update_stock_status(stock)
    elif chosen_command == 2:
        methods.price_listing(stock)
    else:
        methods.category_listing(stock)
