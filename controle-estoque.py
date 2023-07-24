# To open an external terminal: Ctrl + Shift + C
# to run this python file: python controle-estoque.py

stock = []

startOptions = {
    "1": "Iniciar com estoque vazio",
    "2": "Carregar estoque demonstrativo",
    "3": "Fechar o controle de estoque"}

print('\n______________________________________________________\nCONTROLE DE ESTOQUE')
print(f'\n(1) {startOptions["1"]}\n(2) {startOptions["2"]}\n(3) {startOptions["3"]}\n')

while True:
    userInput = input('INSIRA O NÚMERO DO COMANDO DESEJADO: ')
    if userInput in startOptions.keys():
        break



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