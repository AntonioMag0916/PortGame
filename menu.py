import time


class myMenu:
    


    def __init__(self, availableQuestion):
        self.__questions = availableQuestion

    def printStarterInfo(self):
        print("Welcome to PortGame!")
        print("This program was made for the purpose of learning and exploring Git")
        print("You can configure what questions you are asked and what ports are asked")
        print("When you start the game, it ends when you get a question wrong or you exit out")
        time.sleep(1.5)
        print("Now go and test your knowledge!")
        time.sleep(0.5)
        print("\n")

    def printPortInfo(self, ports):
        pass            


    def printHelperInfo(self):
        pass
    
    def startMenu(self):
        options = self.printMenu()
        count = int(options[-1])


        userInput = int(input(f"\nWhat would you like to do?({options}): "))
        
        while ((userInput < 0) or (userInput > count)):
            print(f"Not {options} try again.")
            userInput = int(input(f"What would you like to do?({options}): "))

        print(f"Choosing option {userInput}\n")
        return userInput
    
    def printMenu(self):
        count = 0
        options = ""
        print("Start Game (0)")
        options += f"{count}, "
        count += 1
        print("Display some cool stuff (1)")
        options += f"{count}, "
        count += 1 
        print("Pick specific question (2)")
        options += f"{count}, "
        count += 1
        print("Exit (3)")  
        options += f"or {count}"
        count += 1
        return options


    def coolStuff(self):
        print("\nThis program was written for fun\n")
        time.sleep(1.5)
    
   

    def printQuestionOptions(self):
        options = self.__calculateQuestionOptions()
        count = int(options[-1])


        userInput = int(input(f"\nWhat would you like to do?({options}): "))

        #WE should be sanitizing before input
        while ((userInput < 0) or (userInput > count)):
            print(f"Not {options} try again.")
            userInput = int(input(f"What would you like to do?{options}: "))

        print(f"Choosing Option {userInput}\n")
        time.sleep(0.3)
        return userInput


    def __calculateQuestionOptions(self):
        count = 0  
        options = ""

        print("\nPlease pick one, this will decide what question you get.\n")
        #Eventually a comma separated list will decide too
        time.sleep(0.35)
        #We could just make this into a simple len() check, please refactor dummy
        for question in self.__questions:
            print(str(question.getRawQuestion()) + "(" + str(count) + ")" )
            
            options += str(count) + ", "
            count += 1

            time.sleep(0.70)

        print("All (" + str(count) + ")")
        options += "or " + str(count)
        count += 1
        return options






        



