import random
import math
import time

class qMaker:
    
    #Initalization of a first question
    def __init__(self, questions):
        self.__masterQuestions = questions.copy()
        #Choose one question out of the array
        
    def setQuestions(self, questions):
        
        
        if(type(questions) == type(self.__masterQuestions[0])):
            self.__masterQuestions.clear()
            self.__masterQuestions.append(questions)
        else:
            self.__masterQuestions.clear()
            self.__masterQuestions = questions.copy()
        

    def startQuestions(self):
        self.__startup()
        self.askQuestions()
    

    #Handles starting to ask the new questions
    def askQuestions(self):
        
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
            

    
    def __startup(self):
        print("Startup done")
        self.__questions = self.__masterQuestions.copy()
        self.__score = 0
        self.__correctQuestions = []
        self.__currentQuestion = self.__selectNewQuestion()

        for question in self.__questions:
            question.resetQuestion()

    #(might need change)
    def __selectNewQuestion(self):
        
        if (len(self.__questions) == 1):
            return self.__questions[0]
        else:
            questionsLen = len(self.__questions)
            index = math.floor(random.random() * questionsLen)
            return self.__questions[index]
    
    def __printAnswers(self):
        
        #Print all correct answers
        
        print("\nYour final score was: " + str(self.__score))
        time.sleep(1.5)
        
        
        print("\nCorrect answers: ")

        if (self.__score == 0):
            print("None.")
            time.sleep(0.75)
        else:
            for correctQuestion in self.__correctQuestions:
                print(correctQuestion)
                time.sleep(0.75)

    def __continueQuestions(self):
        self.__currentQuestion = self.__selectNewQuestion()
        self.askQuestions()  
    
