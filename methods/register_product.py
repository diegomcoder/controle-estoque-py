from .update_stock_status import update_stock_status
import os

# REGISTER FIRST PRODUCTS
def register_product(stock):
    os.system("cls")
    print("🔴 CADASTRO DE NOVO PRODUTO:")
    print()
    print('Digite "cancelar" para cancelar o cadastro e voltar ao inventário de estoque\n')
    
    category = input("CATEGORIA: ")
    if category == "cancelar":
        return update_stock_status(stock)
    code = input("CÓDIGO: ")
    if code == "cancelar":
        return update_stock_status(stock)
    name = input("PRODUTO: ")
    if name == "cancelar":
        return update_stock_status(stock)
    description = input("DESCRIÇÃO: ")
    if description == "cancelar":
        return update_stock_status(stock)
    price = input("PREÇO UNITÁRIO: ")
    if price == "cancelar":
        return update_stock_status(stock)
    else:
        price = float(price)
    amount = input("QUANTIDADE: ")
    if amount == "cancelar":
        return update_stock_status(stock)
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
    return update_stock_status(stock)