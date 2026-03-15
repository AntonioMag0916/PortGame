import time


class myMenu:
    


    def __init__(self, availableQuestion, availablePorts):
        self.__questions = availableQuestion
        self.__portLists = availablePorts

    def printStarterInfo(self):
        print("Welcome to PortGame!")
        print("Go and test your knowledge!")
        time.sleep(0.5)
        print("\n")

    def printPortInfo(self, ports):
        c = 1
        for port in ports:
            print(f"{c}. "
                  f"Name: {port.getProtocolName()}, "
                  f"Number: {port.getPortNum()}, "
                  f"Transmission: {port.getTransmissionType()}")
            c += 1
            time.sleep(.35)
        print("\n")

    
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
        print(f"Start Game ({count})")
        options += f"{count}, "
        count += 1
        print(f"Pick ports ({count})")
        options += f"{count}, "
        count += 1 
        print(f"Pick specific question ({count})")
        options += f"{count}, "
        count += 1
        print(f"Display port information ({count})")
        options += f"{count}, "
        count += 1
        print(f"Exit ({count})")  
        options += f"or {count}"
        count += 1
        return options


    def coolStuff(self):
        print("\nThis program was written for fun\n")
        time.sleep(1.5)

    def printPortOptions(self):
        options = self.__calculatePortOptions()
        count = int(options[-1])


        userInput = int(input(f"\nWhat would you like to do?({options}): "))

        #WE should be sanitizing before input
        while ((userInput < 0) or (userInput > count)):
            print(f"Not {options} try again.")
            userInput = int(input(f"What would you like to do?{options}: "))

        print(f"Choosing Option {userInput}\n")
        time.sleep(0.3)
        return userInput

    #For Selecting type of question 61-98ish
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

    def __calculatePortOptions(self):
        count = 0
        options = ""

        print("\nPlease pick one, this will decide what ports you get.\n")

        time.sleep(0.35)
        #We could just make this into a simple len() check, please refactor dummy
        for portList in self.__portLists:
            ports = ""
            for port in portList:
                ports += f"{port.getProtocolName()} "
            ports = ports.rstrip()
            ports = ports.replace(" ", ",")
            print(f"{ports} ({count})")
            
            if (portList != self.__portLists[-1]):
                options += str(count) + ", "
            else:
                options += f"or {count}"
            
            count += 1
            time.sleep(0.70)

        return options

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






        



