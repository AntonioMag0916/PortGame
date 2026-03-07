import random
import math
import re

#(Input validation needed)
class portQuestion:
    def __init__(self, question, ports, questionType, answerType):
        self.__ports = ports.copy()
        self.__question = question
        self.__currentIndex = self.__selectNewPort() 
        self.__currentPort = self.__ports[self.__currentIndex]
        self.__qType = questionType
        self.__aType = answerType
        self.__formattedQuestion = self.__formatQuestion()
        
    

    def askQuestion(self):
        self.__formattedQuestion = self.__formatQuestion()
        return self.__formattedQuestion
    
    def getFormattedQuestion(self):
        return self.__formattedQuestion

    #A type 0 = port, 1 = transmission, 2 = acryonym (What is the answer?)
    #Later add validation
    #Checks userinput against the correct answer
    def checkAnswer(self, userInput):
        
        userInput = userInput.upper()
        match self.__aType:
            case 0:
                return (userInput == self.__currentPort.getPortNum())
            case 1:
                return self.__checkTransmission(userInput)
            case 2: 
                return (userInput == self.__currentPort.getAcronym()) 


    #Just returns the correct answer
    def findCorrect(self):
        match self.__aType:
            case 0:
                return str(self.__currentPort.getPortNum())
            case 1:
                return self.__currentPort.getTransmissionType()
            case 2: 
                return self.__currentPort.getAcronym()

    def getPortLength(self):
        return len(self.__ports)

    #Q type 0 = port, 1 = tranmsission, 2 = acryonym (what is integrated in the question)
    #What is the port num of HTTP? Q type would be 2
    #This function simplfy creates the output for the question depending on what the question is asking and how it is asking it
    def __formatQuestion(self):
        match self.__qType:
            case 0:
                return self.__question + str(self.__currentPort.getPortNum())
            case 1: 
                return self.__question + self.__currentPort.getTransmissionType()
            case 2: 
                return self.__question + self.__currentPort.getAcronym()
            

    def __selectNewPort(self):

        portsLen = len(self.__ports)
        return math.floor(random.random() * portsLen)
        
    def updatePort(self):
        self.__ports.pop(self.__currentIndex)
        self.__currentIndex = self.__selectNewPort()
        self.__currentPort = self.__ports[self.__currentIndex]



    #Helper functions
    def __checkTransmission(self, input):
        tType = re.split(r'\W', self.__currentPort.getTransmissionType())

        #Have this ignore cases later
        if (len(tType) == 2):
            return (input == tType[0] or input == tType[1])
        else:
            return input == tType[0]

