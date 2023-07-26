def get_physical_balance(stock):
    amount = 0

    for category in stock:
        for product in stock[category]:
            amount += product["Amount"]
    return amount