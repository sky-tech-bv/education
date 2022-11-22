class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    def set_year_model(self, year_model):
        self.__year_model = year_model
    
    def set_make(self, make):
        self.__make = make
    
    def accelerating(self):
        self.__speed += 5
        
    def breaking(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed