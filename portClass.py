#Some stuff to note, _ infront of a function means that it is protected
# __ in front of a function or variable means its protected
#More stuff

class port:
    def __init__(self, acronym, portNum, spelledOut, desc):
        #pass = null operator
        self.__acronym = acronym
        self.__portNum = portNum
        self.__spelledOut = spelledOut
        self.__desc = desc

    #the return f thing allow you to put {} and variables in stuff
    def getAcronym(self):
        return f"{self.__acronym}"
    def setAcronum():
        pass
    def getPortNum():
        pass
    def setPortNum():
        pass
    def getSpelledOut():
        pass
    def setSpelledOut():
        pass
    def getDesc():
        pass
    def setDesc():
        pass
    
    