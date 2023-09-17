# descrição, preço unitario, categoria
class Product:
    def __init__(self, name, category, description, unitary_price, quantity_in_stock):
        self.__set_name(name)
        self.__set_category(category)
        self.__set_description(description)
        self.__set_price(unitary_price)
        self.__set_quantity(quantity_in_stock)
        
    def __set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def __set_category(self, category):
        self.__category = category
        
    def get_category(self):
        return self.__category
    
    def __set_description(self, description):
        self.__description = description
        
    def get_description(self):
        return self.__description
    
    def __set_price(self, unitary_price):
        self.__unitary_price = unitary_price
    
    def get_price(self):
        return self.__unitary_price
    
    def __set_quantity(self, quantity):
        self.__quantity_in_stock = quantity
        
    def get_quantity(self):
        return self.__quantity_in_stock