import random
import math

class qMaker:
    
    #Initalization of a first question
    def __init__(self, questions):
        self.__questions = questions
        self.__currentQuestion = self.__selectNewQuestion()
        self.__score = 0
        self.__correctQuestions = []
    
    #Handles starting to ask the new questions
    def startQuestions(self):
        #answer will be different depending on the aType
        answer = input(self.__currentQuestion.askQuestion() + "?: ")
        #currentScore = self.__score - this will eventually be used if pausing or whatnot

        #Continues until the user is wrong (later add other stops)
        #Answer calculation will be based off a function
        if (self.__currentQuestion.checkAnswer(answer)):
            
            correctQuestion = str(self.__currentQuestion.getFormattedQuestion()) + " : " + str(answer)
            self.__correctQuestions.append(correctQuestion)
            self.__score += 1
            print("Correct!\n")
            self.__currentQuestion.updatePort()

            self.__currentQuestion = self.__selectNewQuestion()
            self.startQuestions()
        else:
            print("Incorrect, the answer was: " + str(self.__currentQuestion.findCorrect()))
            print("\nYour final score was: " + str(self.__score))
            print("\nCorrect answers: ")
            for x in self.__correctQuestions:
                print(x)

    def __selectNewQuestion(self):
        questionsLen = len(self.__questions)
        index = math.floor(random.random() * questionsLen)
        return self.__questions[index]

    


#This needs a port list and a string for the question
#This might be used if i need to check out for type of question it is incase i want to do input validation
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
    def checkAnswer(self, userInput):
        match self.__aType:
            case 0:
                return (userInput == self.__currentPort.getPortNum())
            case 1:
                return (userInput == self.__currentPort.getTransmissionType())
            case 2: 
                return (userInput == self.__currentPort.getAcronym()) 

    def findCorrect(self):
        match self.__aType:
            case 0:
                return str(self.__currentPort.getPortNum())
            case 1:
                return self.__currentPort.getTransmissionType()
            case 2: 
                return self.__currentPort.getAcronym()

    #Q type 0 = port, 1 = tranmsission, 2 = acryonym (what is integrated in the question)
    #What is the port num of HTTP? Q type would be 2
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
        #return self.__ports[index]
        

    

    #Removes the current port
    #
    #def __removePort(self):   
    def updatePort(self):

        portsLen = len(self.__ports)
        

        self.__ports.pop(self.__currentIndex)
        self.__currentIndex = self.__selectNewPort()
        self.__currentPort = self.__ports[self.__currentIndex]


#We ask the question 
#after that check if correct or not
#if it is correct, then we go to the question and remove the port from that question then continue
#"What is the port number of " + variable "?: "