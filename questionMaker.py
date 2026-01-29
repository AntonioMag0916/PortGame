import random
import math

class qMaker:


    def __init__(self, questions, ports):
        self.__questions = questions
        self.__ports = ports
        self.__currentPort = self.selectNewPort()
        self.__currentQuestion = self.selectNewQuestion()

       
    

    def randomQuestion(self):
        
        answer = 
        

    def __selectNewQuestion(self):
        questionsLen = len(self.__questions)
        index = math.floor(random.random() * questionsLen)
        return self.__questions[index]

    def __selectNewPort(self):
        
        portsLen = len(self.__ports)
        index = math.floor(random.random() * portsLen)
        return self.__ports[index]


#This might be used if i need to check out for type of question it is incase i want to do input validation
class question:
    def __init__(self):
        pass