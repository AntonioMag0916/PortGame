import time


class myMenu:
    
    def __init__(self, availableQuestion):
        self.__questions = availableQuestion
        

    def startMenu(self):
        self.printMenu()

        userInput = int(input("\nWhat would you like to do?(0, 1, 2, or 3): "))
        
        while ((userInput != 0) and (userInput != 1) and (userInput != 2) and (userInput != 3)):
            print("Not 0, 1, 2, or 3 try again.")
            userInput = int(input("What would you like to do?(0, 1, 2, or 3): "))

        return userInput
    
    def printMenu(self):
        print("Start Game (0)")
        print("Display some cool stuff (1)")
        print("Pick specific question (2)")
        print("Exit (3)")  


    def coolStuff(self):
        print("\nThis program was written for fun\n")
        time.sleep(1.5)
        
    def printQuestionPicker(self):
        count = 0

        print("\nPlease pick one, this will decide what question you get.\n")
        #Eventually a comma separated list will decide too
        time.sleep(0.5)
        for question in self.__questions:
            print(str(question.getRawQuestion()) + "(" + str(count) + ")" )
            count += 1
            time.sleep(0.75)

        print("All (" + str(count) + ")\n")





        



