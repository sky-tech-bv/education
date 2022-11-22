class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, right_answer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__right_answer = right_answer
        
    def set_question(self, question):
        self.__question = question
    
    def set_answer1(self, answer1):
        self.__answer1 = answer1
        
    def self_answer2(self,answer2):
        self.__answer2 =answer2
    
    def set_answer3(self, answer3):
        self.__answer3 = answer3
    
    def set_answer4(self, answer4):
        self.__answer4 = answer4
        
    def set_right_answer(self, right_answer):
        self.__right_answer = right_answer

    def get_answer1(self):
        return self.__answer1
    
    def get_answer2(self):
        return self.__answer2
    
    def get_answer3(self):
        return self.__answer3
    
    def get_answer4(self):
        return self.__answer4
        
    def get_right_answer(self):
        return self.__right_answer
        