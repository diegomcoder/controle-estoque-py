import pandas as pd
import os

stock = {}

# START OF THE PROGRAM
def main():
    os.system("cls")
    print("🔴 BEM VINDO!\n")
    print("(1) Iniciar com estoque vazio")
    print("(2) Carregar estoque demonstrativo")
    print("(3) Fechar o controle de estoque")

    amountOfOptions = 3
    userCommand = getUserCommand(amountOfOptions)

    if userCommand == "3":
        exitProgram()
    elif userCommand == "2":
        loadDemoStock()
        updateStockStatus()
    else:
        updateStockStatus()

# TAKE AS IMPUT THE NUMBER OF SELECTABLE COMMANDS AND RETURN A NUMBER THAT REPRESENTS THE USER'S CHOICE
def getUserCommand(param):
    optionsNumbers = []

    for i in range(param):
        optionsNumbers.append(f"{i +1}")
    
    while True:
        userInput = input('\nINSIRA O NÚMERO DO COMANDO DESEJADO AQUI 👉 ')
        if userInput in optionsNumbers:
            return userInput

# LOADS A DEMONSTRATIVE STOCK THAT'S STORED ON AN EXTERNAL JSON FILE
def loadDemoStock():
    import json
    with open("./data/demo_stock.json", encoding='utf-8') as my_json:
        global stock
        stock = json.load(my_json)

    os.system("cls")
    print("ESTOQUE DEMONSTRATIVO CARREGADO!")

# TAKES A CATEGORY AS INPUT AND RETURNS AN ARRAY WITH ITS PRODUCTS AMOUNT AND ITS PRODUCTS BALANCE
def getAmountAndBalance(category):
    amount = 0
    balance = 0

    for product in stock[category]:
        
        amount += product["Amount"]
        print(f'Produto: {product["Name"]}; Preço: {product["Price"]}; Quantidade: {product["Amount"]}')
        balance += float(product["Price"]) * int(product["Amount"])
        return [f"{amount} produtos | ", f"R$ {round(balance, 2)}"]

def getPhysicalBalance():
    amount = 0
    global stock
    for category in stock:
        for product in stock[category]:
            amount += product["Amount"]
    return amount

def getMonetaryBalance():
    stockValue = 0
    global stock
    for category in stock:
        for product in stock[category]:
            stockValue += float(product["Price"])
    return round(stockValue, 2)


# UPTADE STOCK STATUS
def updateStockStatus():
    physicalBalance = 0
    monetaryBalance = 0
    columns = ["SALDO FÍSICO | ", "SALDO MONETÁRIO"]
    rows = []
    data = []
    global stock
    

    for category in stock:
        rows.append(category)
        data.append(getAmountAndBalance(category))

    physicalBalance = getPhysicalBalance()
    monetaryBalance = getMonetaryBalance()
    
    # os.system("cls")
    # print("Inside updateStockStatus\n", stock)
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
    userCommand = getUserCommand(amountOfOptions)

    if userCommand == "4":
        exitProgram()
    elif userCommand == "3":
        stockQuery()
    elif userCommand == "2":
        registerProduct()
    else:
        updateStockStatus()

# STOCK QUERY
def stockQuery():
    os.system("cls")
    print("AMBIENTE DE CONSULTA DE ESTOQUE")

# REGISTER FIRST PRODUCTS
def registerProduct():
    os.system("cls")
    print("🔴 CADASTRO DE NOVO PRODUTO:")
    print()
    print('Digite "cancelar" para cancelar o cadastro e voltar ao inventário de estoque\n')
    
    category = input("CATEGORIA: ")
    if category == "cancelar":
        return updateStockStatus()
    code = input("CÓDIGO: ")
    if code == "cancelar":
        return updateStockStatus()
    name = input("PRODUTO: ")
    if name == "cancelar":
        return updateStockStatus()
    description = input("DESCRIÇÃO: ")
    if description == "cancelar":
        return updateStockStatus()
    price = input("PREÇO UNITÁRIO: ")
    if price == "cancelar":
        return updateStockStatus()
    else:
        price = float(price)
    amount = input("QUANTIDADE: ")
    if amount == "cancelar":
        return updateStockStatus()
    else:
        amount = int(amount)
    
    newProduct = { "Code": code, "Name": name, "Description": description, "Price": price, "Amount": amount}
    global stock

    if category in stock:
        stock[category].append(newProduct)
    else:
        stock[category] = [newProduct]

    print("\n✅ PRODUTO CADASTRADO\n")
    print("Inside registerProduct\n", stock)
    print('Pressione "ENTER"')
    input()
    return updateStockStatus()

# EXIT PROGRAM
def exitProgram():
    os.system("cls")
    print("\nATÉ MAIS! 😊\n")

# CALL THE START OF THE PROGRAM
main()