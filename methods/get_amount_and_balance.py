# TAKES A CATEGORY AS INPUT AND RETURNS AN ARRAY WITH ITS PRODUCTS AMOUNT AND ITS PRODUCTS BALANCE
def get_amount_and_balance(stock, category):
    amount = 0
    balance = 0

    for product in stock[category]:
        amount += product["Amount"]
        # print(f'Produto: {product["Name"]}; Preço: {product["Price"]}; Quantidade: {product["Amount"]}')
        balance += float(product["Price"]) * int(product["Amount"])
        return [f"{amount} produtos | ", f"R$ {round(balance, 2)}"]