import random
import math
import time

class qMaker:
    
    #Initalization of a first question
    def __init__(self, questions):
        self.__questions = questions
        #Choose one question out of the array
        self.__currentQuestion = self.__selectNewQuestion()
        self.__score = 0
        self.__correctQuestions = []
    

    #Handles starting to ask the new questions
    def startQuestions(self):
        
        #answer will be different depending on the aType
        answer = input(self.__currentQuestion.askQuestion() + "?: ")
        

        #Calculates Answer using the currentQuestion object
        if (self.__currentQuestion.checkAnswer(answer)):
            
            self.__score += 1
            print("Correct!\n")
            
            correctQuestion = str(self.__score) + ". " + str(self.__currentQuestion.getFormattedQuestion()) + " : " + str(answer)
            self.__correctQuestions.append(correctQuestion)
            
            #if there are no ports in the question
            #This function could probably look a lot better
            if (self.__currentQuestion.getPortLength() == 1):
                
                #Remove the question
                self.__questions.pop(self.__questions.index(self.__currentQuestion))

                #If no questions left, end, else, return to normal
                if (len(self.__questions) == 0):
                    print("No questions remaining!")
                    self.__printAnswers()
                else:
                    self.__continueQuestions()
            else:
                self.__currentQuestion.updatePort()
                self.__continueQuestions()

           
        else:
            print("Incorrect, the answer was: " + str(self.__currentQuestion.findCorrect()))
            
            self.__printAnswers()
            

    #(might need change)
    def __selectNewQuestion(self):
        questionsLen = len(self.__questions)
        index = math.floor(random.random() * questionsLen)
        return self.__questions[index]
    
    def __printAnswers(self):
        #Print all correct answers
        print("\nYour final score was: " + str(self.__score))
        print("\nCorrect answers: ")

        for correctQuestion in self.__correctQuestions:
            print(correctQuestion)
            time.sleep(0.5)

    def __continueQuestions(self):
        self.__currentQuestion = self.__selectNewQuestion()
        self.startQuestions()  
    
