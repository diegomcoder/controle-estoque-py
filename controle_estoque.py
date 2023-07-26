import pandas as pd
import os

stock = []

# START OF THE PROGRAM
def main():
    os.system("Clear")
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

    os.system("Clear")
    print("ESTOQUE DEMONSTRATIVO CARREGADO!")

# TAKES A CATEGORY AS INPUT AND RETURNS AN ARRAY WITH ITS PRODUCTS AMOUNT AND ITS PRODUCTS BALANCE
def getAmountAndBalance(category):
    amount = 0
    balance = 0

    for product in stock[category]:
        
        amount += product["Amount"]
        balance += round(product["Price"] * product["Amount"], 2)
        return [f"{amount} produtos", f"R$ {balance}"]
        
# UPTADE STOCK STATUS
def updateStockStatus():
    physicalBalance = 0
    monetaryBalance = 0
    columns = ["SALDO FÍSICO", "SALDO MONETÁRIO"]
    rows = []
    data = []

    for category in stock:
        rows.append(category)
        data.append(getAmountAndBalance(category))
    
    os.system("Clear")
    print("🔴 INVENTÁRIO DE ESTOQUE AGORA:\n_________________________________________")

    tabela = pd.DataFrame(data=data, index=rows, columns=columns)
    print(tabela)

    print("_________________________________________\n")
    print(f"TOTAL DE PRODUTOS: {physicalBalance}")
    print(f"VALOR DE ESTOQUE: R$ {monetaryBalance}")
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
    os.system("Clear")
    print("AMBIENTE DE CONSULTA DE ESTOQUE")

# REGISTER FIRST PRODUCTS
def registerProduct():
    os.system("Clear")
    print("AMBIENTE DE CADASTRO DE NOVO PRODUTO")

# EXIT PROGRAM
def exitProgram():
    os.system("Clear")
    print("\nATÉ MAIS! 😊\n")

# CALL THE START OF THE PROGRAM
main()