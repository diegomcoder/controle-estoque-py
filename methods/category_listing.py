import methods
from modules import *
import json
with open('./data/msg.json', encoding="utf-8") as my_json:
    msg = json.load(my_json)

lang = "pt"
msg = msg[lang]

def print_existing_categories(stock):
    os.system("cls")
    print(msg["existing_categories"])
    for category in stock:
        print(category)

def category_listing(stock):
    print_existing_categories(stock)

    chosen_category = methods.prompt_user_for_data("^.{3,}$", msg["enter_desired_category"])

    print()
    if chosen_category in stock:
        data = []
        columns = ["  CÓDIGO", "  QUANTIDADE", "  PREÇO UNITÁRIO", "  VALOR DE ESTOQUE"]
        rows = []

        os.system("cls")
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
        methods.print_menu("list_other_category", "List_by_price", "back_to_inventory", "exit_stock_control")

        input_text = methods.prompt_user_for_data("^[1-4]$", msg["enter_command"])
        chosen_command = int(input_text)

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
        input('\n🚫 Essa categoria não existe :-(\n\nPressione "Enter" para continuar  ')
        category_listing(stock)


