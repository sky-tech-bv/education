class Procedure:
    def __init__(self, proced_name, date, doct_name, price):
        self.__proced_name = proced_name
        self.__date = date
        self.__doct_name = doct_name
        self.__price = price
        
    def set_proced_name(self, proced_name):
        self.__proced_name = proced_name
    
    def set_date(self, date):
        self.__date = date
        
    def self_doct_name(self, doct_name):
        self.__doct_name = doct_name
    
    def set_price(self, price):
        self.__price = price
    
    def get_proced_name(self):
        return self.__proced_name
    
    def get_date(self):
        return self.__date
    
    def get_doct_name(self):
        return self.__doct_name
    
    def get_price(self):
        return float(self.__price)