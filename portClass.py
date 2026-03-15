#Some stuff to note, _ infront of a function means that it is protected
# __ in front of a function or variable means its protected
#More stuff

class port:
    def __init__(self, protocolName, portNum, spelledOut, transmissionType, desc):
        #pass = null operator
        self.__protocolName = protocolName
        self.__portNum = portNum
        self.__spelledOut = spelledOut
        self.__transType = transmissionType
        self.__desc = desc
        

    #the return f thing allow you to put {} and variables in stuff
    def getProtocolName(self):
        return f"{self.__protocolName}"
    def _setProtocolName(self, newAcronum):
        self.__protocolName = newAcronum

    def getPortNum(self):
        return f"{self.__portNum}"
    def _setPortNum(self, newPortNum):
        self.__portNum = newPortNum

    def getSpelledOut(self):
        return f"{self.__spelledOut}"
    def _setSpelledOut(self, newSpelledOut):
        self.__spelledOut = newSpelledOut

    def getTransmissionType(self):
        return f"{self.__transType}"
    def _setTransmissionType(self, newTransType):
        self.__transType = newTransType

    def getDesc(self):
        return f"{self.__desc}"
    def _setDesc(self, newDesc):
        self.__desc = newDesc

    
    