import methods
import os

# REGISTER FIRST PRODUCTS
def register_product(stock):
    print("\n\n\n")
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
        try:
            price = float(price)
        except ValueError:
            os.system("cls")
            print("\n🚫 ERRO:\n")
            print("O preço tem que ser um número inteiro positivo\n\n\n\n")
            input('Pressione "ENTER" para recomeçar o cadastro... ')
            register_product(stock)
            return

    print(price)

    amount = input("QUANTIDADE: ")
    if amount == "cancelar":
        methods.update_stock_status(stock)
        return
    else:
        try:
            amount = int(amount)
        except ValueError:
            os.system("cls")
            print("\n🚫 ERRO:\n")
            print("A quantidade tem que ser um numero natural\n\n\n\n")
            input('Pressione "ENTER" para recomeçar o cadastro... ')
            register_product(stock)
            return
    
    newProduct = { "Code": code, "Name": name, "Description": description, "Price": price, "Amount": amount}

    if category in stock:
        stock[category].append(newProduct)
    else:
        stock[category] = [newProduct]

    print("\n✅ PRODUTO CADASTRADO\n\n")
    input('Pressione "ENTER" para continuar ')
    return methods.update_stock_status(stock)