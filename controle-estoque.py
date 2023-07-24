# To open an external terminal: Ctrl + Shift + C
# to run this python file: python controle-estoque.py

stock = []

# START OF THE PROGRAM
def main():
    userName = input("\nQual o seu nome? ")

    print(f'\n______________________________________________________\n\nSeja bem vindo (a) {userName} 😉')
    print('\n(1) Iniciar com estoque vazio\n(2) Carregar estoque demonstrativo\n(3) Fechar o controle de estoque\n')

    while True:
        userInput = input('INSIRA O NÚMERO DO COMANDO DESEJADO: ')
        if userInput in ["1", "2", "3"]:
            break

    if userInput == "3":
        print("\n\nATÉ MAIS! 😊\n")
        return
    elif userInput == "2":
        loadDemoStock()
    else:
        registerProduct()

# LOAD DEMONSTRATIVE STOCK
def loadDemoStock():
    print("\n______________________________________________________\nBEM VINDO AO CONTROLE DE ESTOQUE!")
    print("\nESTOQUE DEMONSTRATIVO CARREGADO!\nSaldo de estoque: 439 produtos\nQuantidade de categorias: 25\nSaldo monetário de estoque: R$ 315.087,00\n")

# REGISTER FIRST PRODUCTS
def registerProduct():
    print("\n______________________________________________________\nBEM VINDO AO CONTROLE DE ESTOQUE!")
    print("\nCADASTRE O SEU PRIMEIRO PRODUTO\n")
    print('\n(1) Sim, cadastrar um produto\n(2) Voltar ao menu anterior\n(3) Fechar o controle de estoque\n')

# CALL THE START OF THE PROGRAM
main()