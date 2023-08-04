import methods
from modules import *

def price_listing(stock):

    os.system("cls")

    minimum_price = 0
    maximum_price = 0

    for category in stock:
        for product in stock[category]:
            if minimum_price == 0:
                minimum_price = product["Price"]

            elif product["Price"] < minimum_price:
                minimum_price = product["Price"]

            if product["Price"] > maximum_price:
                maximum_price = product["Price"]

    print("\n🔴 AMPLITUDE DE PREÇOS:")
    print(f"Preço mínimo: R$ {minimum_price}")
    print(f"Preço máximo: R$ {maximum_price}")

    print()

    while True:
        user_minimum_price = input("\nDigite o preço mínimo aqui 👉")
        user_minimum_price = float(user_minimum_price)
        if user_minimum_price < minimum_price:
            print(f"\nPreço inválido! Escolha um valor entre {minimum_price} e {maximum_price}.")
        else:
            break

    while True:
        user_maximum_price = input("\nDigite o preço máximo aqui 👉")
        user_maximum_price = float(user_maximum_price)
        if user_maximum_price > maximum_price:
            print(f"\nPreço inválido! Escolha um valor entre {user_minimum_price} e {maximum_price}.")
        else:
            break

    data = []
    columns = ["  CÓDIGO", "  QUANTIDADE", "  PREÇO UNITÁRIO", "  VALOR DE ESTOQUE"]
    rows = []
    
    os.system("cls")
    print(f"🔴 PRODUTOS ENTRE R$ {user_minimum_price} E R$ {user_maximum_price}:")

    for category in stock:
        for product in stock[category]:
            if user_minimum_price <= product["Price"] <= user_maximum_price:
                product_code = product["Code"]
                unitary_price = product["Price"]
                product_amount = product["Amount"]
                total_balance = round(product_amount * unitary_price, 2)

                if len(product["Name"]) > 20:
                    rows.append(f'{product["Name"][0:17]}' + "...")
                else:
                    rows.append(product["Name"])

                data.append([product_code, f"{product_amount} produtos", f"R$ {round(unitary_price, 2)}", f"R$ {total_balance}"])

    table = pandas.DataFrame(data=data, index=rows, columns=columns)

    print()
    print(table)
    print()
    print("(1) Listar produtos segundo outra faixa de preços")
    print("(2) Listar produtos de uma categoria")
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
        methods.category_listing(stock)
    else:
        price_listing(stock)
