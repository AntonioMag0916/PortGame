import time


class myMenu:
    

    
    def startMenu(self):
        self.printMenu()

        userInput = int(input("\nWhat would you like to do?(0, 1, or 2): "))
        
        while ((userInput != 0) and (userInput != 1) and (userInput != 2)):
            print("Not 0, 1, or 2, try again.")
            userInput = int(input("What would you like to do?(0, 1, or 2): "))

        return userInput
    
    def printMenu(self):
        print("Start Game (0)")
        print("Display some cool stuff (1)")
        print("Exit (2)")  


    def coolStuff(self):
        print("\nThis program was written for fun\n")
        time.sleep(1.5)
        




        



