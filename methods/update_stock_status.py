from methods import get_user_command
from methods import get_amount_and_balance
from methods import exit_program
from methods import stock_query
from methods import register_product
from methods import get_physical_balance
from methods import get_monetary_balance
import pandas as pd
import os

# UPTADE STOCK STATUS
def update_stock_status(stock):
    physicalBalance = 0
    monetaryBalance = 0
    columns = ["SALDO FÍSICO | ", "SALDO MONETÁRIO"]
    rows = []
    data = []

    for category in stock:
        rows.append(category)
        data.append(get_amount_and_balance(stock, category))

    physicalBalance = get_physical_balance(stock)
    monetaryBalance = get_monetary_balance(stock)
    
    os.system("cls")
    # print("Inside update_stock_status\n", stock)
    print("🔴 INVENTÁRIO DE ESTOQUE AGORA:")

    if physicalBalance > 0:
        tabela = pd.DataFrame(data=data, index=rows, columns=columns)
        print("____________________________________________")
        print(tabela)
        print("____________________________________________\n")
        print(f"TOTAL DE PRODUTOS: {physicalBalance}")
        print(f"VALOR DE ESTOQUE: R$ {monetaryBalance}")
    else:
        print("\n⚠️ Sem produtos em estoque!")

    print()
    print("(1) Atualizar inventário de estoque")
    print("(2) Cadastrar um novo produto")
    print("(3) Fazer uma consulta de estoque")
    print("(4) Fechar o controle de estoque")

    amountOfOptions = 4
    userCommand = get_user_command(amountOfOptions)

    if userCommand == "4":
        exit_program()
    elif userCommand == "3":
        stock_query(stock)
    elif userCommand == "2":
        register_product(stock)
    else:
        update_stock_status(stock)