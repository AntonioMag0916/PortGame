import random
import math

class qMaker:

    
    def __init__(self, questions, ports):
        self.__questions = questions
        self.__ports = ports
        self.__currentPort = self.__selectNewPort()
        self.__currentQuestion = self.__selectNewQuestion()
        self.__score = 0

       
    

    def randomQuestion(self):
        
        answer = input(self.__currentQuestion + self.__currentPort.getAcronym() + "?: ")
        currentScore = self.__score

        if (answer == self.__currentPort.getPortNum()):
            self.__score += 1
            print("Correct!\n")
            self.__currentPort = self.__selectNewPort()
            self.randomQuestion()
        else:
            print("Incorrect, the answer was: " + str(self.__currentPort.getPortNum()))
            print("\nYour final score was: " + str(self.__score))

            
        
        
    



    def __selectNewQuestion(self):
        questionsLen = len(self.__questions)
        index = math.floor(random.random() * questionsLen)
        return self.__questions[index]

    def __selectNewPort(self):
        
        portsLen = len(self.__ports)
        index = math.floor(random.random() * portsLen)
        return self.__ports[index]


#This needs a port list and a string for the question
#This might be used if i need to check out for type of question it is incase i want to do input validation
class question:
    def __init__(self, question, ports):
        self.__ports = ports
        self.__question = question

    
