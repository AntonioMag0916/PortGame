import random
import math

class qMaker:
    
    #Initalization of a first question
    def __init__(self, questions):
        self.__questions = questions
        self.__currentQuestion = self.__selectNewQuestion()
        self.__score = 0
    
    #Handles starting to ask the new questions
    def randomQuestion(self):
        

        #answer will be different depending on the aType
        #answer = input(self.__currentQuestion + self.__currentQuestion + "?: ")
        #currentScore = self.__score - this will eventually be used if pausing or whatnot

        #Continues until the user is wrong (later add other stops)
        #Answer calculation will be based off a function
        if (answer == self.__currentPort.getPortNum()):
            self.__score += 1
            print("Correct!\n")

            self.__currentQuestion = self.__selectNewQuestion()
            self.randomQuestion()
        else:
            print("Incorrect, the answer was: " + str(self.__currentPort.getPortNum()))
            print("\nYour final score was: " + str(self.__score))

    def __selectNewQuestion(self):
        questionsLen = len(self.__questions)
        index = math.floor(random.random() * questionsLen)
        return self.__questions[index]

    


#This needs a port list and a string for the question
#This might be used if i need to check out for type of question it is incase i want to do input validation
class question:
    def __init__(self, question, ports, questionType, answerType):
        self.__ports = ports
        self.__question = question
        self.__currentIndex = self.__selectNewPort() 
        self.__currentPort = self.__ports[self.__currentIndex]
        self.__qType = questionType
        self.__aType = answerType
        self.formattedQuestion = self.__formatQuestion()
        

    
    def askQuestion(self):
        pass

       


        
    #A type 0 = port, 1 = transmission, 2 = acryonym (What is the answer?)
    def checkAnswer():
        pass


    #Q type 0 = port, 1 = tranmsission, 2 = acryonym (what is integrated in the question)
    #What is the port num of HTTP? Q type would be 2
    def __formatQuestion(self):
        match self.__qType:
            case 0:
                return self.question + str(self.__currentPort.getPortNum()) + "?: "
            case 1: 
                return self.question + self.__currentPort.getTransmissionType() + "?: "
            case 2: 
                return self.question + self.__currentPort.getAcryonym() + "?: "
            

    def __selectNewPort(self):

        portsLen = len(self.__ports)
        return math.floor(random.random() * portsLen)
        #return self.__ports[index]

    

    #Removes the current port
    #
    def __removePort(self):
        self.__ports.pop(self.__currentIndex)
        

    def __updatePort(self):
        self.__currentIndex = self.__selectNewPort()
        self.__currentPort = self.__ports[self.__currentIndex]


#We ask the question 
#after that check if correct or not
#if it is correct, then we go to the question and remove the port from that question then continue
#"What is the port number of " + variable "?: "