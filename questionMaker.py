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
        

        #Calculates Answer using the currentQuestion object
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
            for correctQuestion in self.__correctQuestions:
                print(correctQuestion)

    #(might need change)
    def __selectNewQuestion(self):
        questionsLen = len(self.__questions)
        index = math.floor(random.random() * questionsLen)
        return self.__questions[index]

    
