import methods
from modules import *

# UPTADE STOCK STATUS
def update_stock_status(stock):
    physicalBalance = 0
    monetaryBalance = 0
    columns = ["SALDO FÍSICO | ", "SALDO MONETÁRIO"]
    rows = []
    data = []

    for category in stock:
        rows.append(category)

    data = methods.get_amount_and_balance(stock)

    physicalBalance = methods.get_physical_balance(stock)
    monetaryBalance = methods.get_monetary_balance(stock)
    
    os.system("cls")
    # print("Inside update_stock_status\n", stock)
    print("🔴 INVENTÁRIO DE ESTOQUE AGORA:")

    if physicalBalance > 0:
        tabela = pandas.DataFrame(data=data, index=rows, columns=columns)
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
    userCommand = methods.get_user_command(amountOfOptions)

    if userCommand == "4":
        methods.exit_program()
        return
    elif userCommand == "3":
        methods.stock_query(stock)
    elif userCommand == "2":
        methods.register_product(stock)
    else:
        update_stock_status(stock)