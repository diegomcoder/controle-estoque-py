stock = []

# START OF THE PROGRAM
def main():
    print('___________________________________________________________________________________________________\n')
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

# GET USER'S COMMAND
def getUserCommand(param):
    optionsNumbers = []

    for i in range(param):
        optionsNumbers.append(f"{i +1}")
    
    while True:
        userInput = input('\nINSIRA O NÚMERO DO COMANDO DESEJADO AQUI 👉 ')
        if userInput in optionsNumbers:
            return userInput

# LOAD DEMONSTRATIVE STOCK
def loadDemoStock():
    import json
    with open("./data/demo_stock.json", encoding='utf-8') as my_json:
        global stock
        stock = json.load(my_json)

    print("___________________________________________________________________________________________________")
    print("ESTOQUE DEMONSTRATIVO CARREGADO!")

# UPTADE STOCK STATUS
def updateStockStatus():
    colunas = ["QUANTIDADE EM ESTOQUE", "VALOR EM ESTOQUE"]
    linhas = []
    dados = []

    for category in stock:
        linhas.append(category)
        # print("Categoria: " + category)

        for product in stock[category]:
            # print("Produto: " + product)

            amount = 0
            balance = 0

            amount += product["Amount"]
            balance += round(product["Price"] * product["Amount"], 2)
            dados.append([amount, balance])

    print('___________________________________________________________________________________________________\n')
    print("🔴 INVENTÁRIO DE ESTOQUE AGORA:\n")

    print(colunas)
    print(linhas)
    print(dados)

    """
                    SALDO FÍSICO        SALDO MONETÁRIO
    Audio:          12 produtos         R$ 3434,00
    Móveis:         45 produtos         R$ 838,00
    Games:          45 produtos         R$ 23,00
    Informática:    32 produtos         R$ 8005,87
    Livros:         11 produtos         R$ 238,89
    Mercado:        65 produtos         R$ 189,90

    TOTAL DE PRODUTOS: 3453
    VALOR DE ESTOQUE: R$ 23.902,00

    """
    # print(f"{stock}\n")
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
    print("___________________________________________________________________________________________________")
    print("AMBIENTE DE CONSULTA DE ESTOQUE")

# REGISTER FIRST PRODUCTS
def registerProduct():
    print("___________________________________________________________________________________________________")
    print("AMBIENTE DE CADASTRO DE NOVO PRODUTO")

# EXIT PROGRAM
def exitProgram():
    print("___________________________________________________________________________________________________\n")
    print("ATÉ MAIS! 😊")

# CALL THE START OF THE PROGRAM
main()