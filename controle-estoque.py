# To open an external terminal: Ctrl + Shift + C
# to run this python file: python controle-estoque.py

stock = []

# START OF THE PROGRAM
def main():

    options = {
        "1": "Iniciar com estoque vazio",
        "2": "Carregar estoque demonstrativo",
        "3": "Fechar o controle de estoque"}

    print('\n______________________________________________________\nCONTROLE DE ESTOQUE')
    print(f'\n(1) {options["1"]}\n(2) {options["2"]}\n(3) {options["3"]}\n')

    while True:
        userInput = input('INSIRA O NÚMERO DO COMANDO DESEJADO: ')
        if userInput in options.keys():
            break

    if userInput == "3":
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
    options = {
        "1": "Sim, cadastrar um produto",
        "2": "Voltar ao menu anterior",
        "3": "Fechar o controle de estoque"}
    
    print("\n______________________________________________________\nBEM VINDO AO CONTROLE DE ESTOQUE!")
    print("\nCADASTRE O SEU PRIMEIRO PRODUTO\n")
    print(f'\n(1) {options["1"]}\n(2) {options["2"]}\n(3) {options["3"]}\n')

# CALL THE START OF THE PROGRAM
main()


"""
category = input('Categoria do produto: ')
code = int(input('Código do produto: '))
name = input('Nome do produto: ')
description = input('Descrição do produto: ')
price = input('Preço do produto: ')

print()
print('###############################')
print(f'Categoria do produto: {category}')
print(f'Código do produto: {code}')
print(f'Nome do produto: {name}')
print(f'Descrição do produto: {description}')
print(f'Preço do produto: {price}')
print('###############################')
print()
"""