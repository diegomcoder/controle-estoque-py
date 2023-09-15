# descrição, preço unitario, categoria
class Product:
    def __init__(self, name, price, description):
        self.__name = self.__set_name(name)
        self.__price = self.__set_price(price)
        self.__description = self.__set_description(description)
        
    def __set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def __set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def __set_description(self, description):
        self.__description = description
        
    def get_description(self):
        return self.__description