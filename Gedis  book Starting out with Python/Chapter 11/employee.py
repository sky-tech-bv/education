class Employee:
    def __init__(self, empl_name, empl_numb):
        self.__empl_name = empl_name
        self.__empl_numb = empl_numb
        
    def set_empl_name(self, empl_name):
        self.__empl_name = empl_name
        
    def set_empl_numb(self, empl_numb):
        self.__empl_numb = empl_numb
    
    def get_empl_name(self):
        return self.__empl_name
    
    def get_empl_numb(self):
        return self.__empl_numb
    
class ProductionWorker(Employee):
    def __init__(self, empl_name, enpl_numb, work_id, hour_rate):
        Employee.__init__(self, empl_name, empl_numb)
        self.__work_id = work_id
        self.__hour_rate = hour_rate
        
    def set_work_id(self, work_id):
        self.__work_id = work_id
        
    def set_hour_rate(self, hour_rate):
        self.__hour_rate = hour_rate
        
    def get_work_id(self):
        return self.__work_id
    
    def get_hour_rate(self):
        return self.__hour_rate
    
class ShiftSupervisor(Employee):
    def __init__(self, empl_name, empl_numb, year_salery, year_benefit):
        Employee.__init__(self, empl_name, empl_numb)
        self.__year_salery = year_salery
        self.__year_benefit = year_benefit
        
    def set_year_salery(self, year_salery):
        self.__year_salery = year_salery
        
    def set_year_benefit(self, year_benefit):
        self.__year_benefit = year_benefit
        
    def get_year_salery(self):
        return self.__year_salery
    
    def get_year_benefit(self):
        return self.__year_salery * self.__year_benefit / 100