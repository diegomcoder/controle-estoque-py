import methods
import os

# REGISTER FIRST PRODUCTS
def register_product(stock):
    os.system("cls")
    print("🔴 CADASTRO DE NOVO PRODUTO:")
    print()
    print('Digite "cancelar" para cancelar o cadastro e voltar ao inventário de estoque\n')
    
    category = input("CATEGORIA: ")
    if category == "cancelar":
        methods.update_stock_status(stock)
        return
    code = input("CÓDIGO: ")
    if code == "cancelar":
        methods.update_stock_status(stock)
        return
    name = input("PRODUTO: ")
    if name == "cancelar":
        methods.update_stock_status(stock)
        return
    description = input("DESCRIÇÃO: ")
    if description == "cancelar":
        methods.update_stock_status(stock)
        return
    price = input("PREÇO UNITÁRIO: ")
    if price == "cancelar":
        methods.update_stock_status(stock)
        return
    else:
        price = float(price)
    amount = input("QUANTIDADE: ")
    if amount == "cancelar":
        methods.update_stock_status(stock)
        return
    else:
        amount = int(amount)
    
    newProduct = { "Code": code, "Name": name, "Description": description, "Price": price, "Amount": amount}

    if category in stock:
        stock[category].append(newProduct)
    else:
        stock[category] = [newProduct]

    print("\n✅ PRODUTO CADASTRADO\n")
    # print("Inside register_product\n", stock)
    print('Pressione "ENTER"')
    input()
    return methods.update_stock_status(stock)