import methods
from modules import *

def category_listing(stock):
    os.system("cls")
    print("\nCATEGORIAS EXISTENTES:")

    for category in stock:
        print(category)

    chosen_category = input("\nDigite o nome da categoria desejada aqui 👉")

    print()
    if chosen_category in stock:
        data = []
        columns = ["  CÓDIGO", "  QUANTIDADE", "  PREÇO UNITÁRIO", "  VALOR DE ESTOQUE"]
        rows = []

        print(f"🔴 PRODUTOS DA CATEGORIA {chosen_category.upper()}:")

        for category in stock:
            if category == chosen_category:
                for product in stock[category]:
                    product_code = product["Code"]
                    unitary_price = product["Price"]
                    product_amount = product["Amount"]
                    total_balance = round(product_amount * unitary_price, 2)

                    if len(product["Name"]) > 20:
                        rows.append(f'{product["Name"][0:17]}' + "...")
                    else:
                        rows.append(product["Name"])

                    data.append([product_code, f"{product_amount} produtos", f"R$ {round(unitary_price, 2)}",
                                 f"R$ {total_balance}"])
                table = pandas.DataFrame(data=data, index=rows, columns=columns)
                print()
                print(table)

        print()
        print("(1) Listar produtos de outra categoria")
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
            category_listing(stock)

    else:
        print("Essa categoria não existe :-(\n\n")


