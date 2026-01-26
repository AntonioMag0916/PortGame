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
    def _setAcronum(self, newAcronum):
        self.__acronym = newAcronum
    def getPortNum(self):
        return f"{self.__portNum}"
    def _setPortNum(self, newPortNum):
        self.__portNum = newPortNum
    def getSpelledOut(self):
        return f"{self.__spelledOut}"
    def _setSpelledOut(self, newSpelledOut):
        self.__spelledOut = newSpelledOut
    def getDesc(self):
        return f"{self.__desc}"
    def _setDesc(self, newDesc):
        self.__desc = newDesc
    
    