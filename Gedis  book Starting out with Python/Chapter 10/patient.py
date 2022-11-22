class Patient:
    def __init__(self, name, adress, phone_num, contct_data):
        self.__name = name
        self.__adress = adress
        self.__phone_num = phone_num
        self.__contct_data = contct_data
        
    def set_name(self, name):
        self.__name = name
    
    def set_adress(self, adress):
        self.__adress = adress
        
    def self_phone_num(self, phone_num):
        self.__phone_num = phone_num
    
    def set_contct_data(self, contct_data):
        self.__contct_data = contct_data
    
    def get_name(self):
        return self.__name
    
    def get_adress(self):
        return self.__adress
    
    def get_phone_num(self):
        return self.__phone_num
    
    def get_contct_data(self):
        return self.__contct_data