def get_monetary_balance(stock):
    stockValue = 0

    for category in stock:
        for product in stock[category]:
            stockValue += float(product["Price"]) * int(product["Amount"])
    return round(stockValue, 2)