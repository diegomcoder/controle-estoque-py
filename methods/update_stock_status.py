import methods
from modules import *

# UPTADE STOCK STATUS
def update_stock_status(stock):
    columns = ["    QUANTIDADES", "    SALDO CATEGORIA"]
    rows = []

    for category in stock:
        rows.append(category)

    data = methods.get_amount_and_balance(stock)
    physical_balance = methods.get_physical_balance(stock)
    monetary_balance = methods.get_monetary_balance(stock)

    data.append(["", ""])
    data.append([f"{physical_balance} produtos",f"R$ {monetary_balance}"])
    rows.append("")
    rows.append("TOTAIS")

    print("\n\n\n")
    os.system("cls")
    print("🔴 INVENTÁRIO DE ESTOQUE AGORA:")

    if physical_balance > 0:
        tabela = pandas.DataFrame(data=data, index=rows, columns=columns)
        print("_______________________________________________\n")
        print(tabela)
        print("_______________________________________________\n")
        print()
        print("(1) Atualizar inventário de estoque")
        print("(2) Cadastrar um novo produto")
        print("(3) Fazer uma consulta de estoque")
        print("(4) Fechar o controle de estoque")

        options_amount = 4
        chosen_command = methods.get_user_command(options_amount)

        if chosen_command == 4:
            methods.exit_program()
            return
        elif chosen_command == 3:
            methods.stock_query(stock)
        elif chosen_command == 2:
            methods.register_product(stock)
        else:
            update_stock_status(stock)
    else:
        print("\n⚠️ Sem produtos em estoque!")
        print()
        print("(1) Atualizar inventário de estoque")
        print("(2) Cadastrar um novo produto")
        print("(3) Fechar o controle de estoque")

        options_amount = 3
        chosen_command = methods.get_user_command(options_amount)

        if chosen_command == 3:
            methods.exit_program()
            return
        elif chosen_command == 2:
            methods.register_product(stock)
        else:
            update_stock_status(stock)



