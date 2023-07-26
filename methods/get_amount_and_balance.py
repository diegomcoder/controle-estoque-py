# TAKES A CATEGORY AS INPUT AND RETURNS AN ARRAY WITH ITS PRODUCTS AMOUNT AND ITS PRODUCTS BALANCE
def get_amount_and_balance(stock):
    data = []

    for category in stock:
        amount = 0
        balance = 0

        for product in stock[category]:
            amount += product["Amount"]
            balance += float(product["Price"]) * int(product["Amount"])
        data.append([f"{amount} unidades", f" R$ {round(balance, 2)}"])

    return data