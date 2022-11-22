class Employee:
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title
        
    def set_name(self, name):
        self.__name = name
    
    def set_id_num(self, id_num):
        self.__id_num = id_num
        
    def self_department(self,department):
        self.__department =department
    
    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    def get_name(self):
        return self.__name
    
    def get_id_num(self):
        return self.__id_num
    
    def get_department(self):
        return self.__department
    
    def get_job_title(self):
        return self.__job_title
    
    def __str__(self):
        return f'\tИмя сотрудника: {self.__name}\n' + \
               f'\tИдентификационный номер сотрудника {self.get_name()}: {self.__id_num}\n' + \
               f'\tОтдел, в котором трудится сотредник {self.get_name()}: {self.__department}\n' + \
               f'\tДолжность сотрудника {self.get_name()}: {self.__job_title}'