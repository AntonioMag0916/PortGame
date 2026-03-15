"""
Made by Antonio Magnani

This program was made for the purpose of learning and exploring Git
You can configure what questions you are asked and what ports are asked
When you start the game, it ends when you get a question wrong or you exit out

"""


        

#Port game start, 1/25/26
import portClass
import questionMaker
import questionClass
import menu



http = portClass.port("HTTP", 80, "Hypertext Transfer Protocol", "TCP","Website communication, insecure")
https = portClass.port("HTTPS", 443, "Hypertext Transfer Protocol Secure", "TCP", "Website communication, secure")
smtp = portClass.port("SMTP", 25, "Simple Mail Transfer Protocl", "TCP", "Mail deilvery protocol")
telnet = portClass.port("TELNET", 23, "Telent", "TCP", "Remote access protocol, insecure")
ssh = portClass.port("SSH", 22, "Secure Shell", "TCP/UDP", "Remote access protocol, secure")
dns = portClass.port("DNS", 53, "Domain Name System", "TCP/UDP", "IPs to human readable text")
mysql = portClass.port("MYSQL", 3306, "MySQL", "TCP", "SQL Server")
ftpdata = portClass.port("FTP-DATA", 20, "File Transfer Protocol-Data", "TCP/UDP", "FTP download and upload service")
ftpcon = portClass.port("FTP-CON", 21, "File Transfer Protocol-Control", "TCP/UDP", "Allows for a stateful channel for FTP commands")
#Make one for simple ftp and include both 20/21 to allow naming the acryonum
syslog = portClass.port("SYSLOG", 514, "System Logging", "UDP", "Enables centralized collection of logs and events")
ntp = portClass.port("NTP", 123, "Network Time Protocol", "UDP", "Automatic time update protocol")
smb = portClass.port("SMB", 445, "Server Message Block", "TCP", "Network file sharing protocol")
snmp = portClass.port("SNMP", 161,"Simple Network Management Protocol", "TCP/UDP", "Used to centrally collect and organize data from other network devices")
snmptrap = portClass.port("SNMP-TRAP", 162 ,"Simple Network Management Protocol - Trap", "TCP/UDP", "Unsolicited message from Agent to Manager ")

ports = [http, https, smtp, telnet, ssh, dns, mysql, ftpdata, ftpcon, syslog, ntp]
testPorts = [http, dns, ntp]
commonPorts = [http, https, ssh, dns, ntp, smtp, smb, telnet] #Startoff with 8
#Think of more port lists

"""
---Needed Updates---
-Refactor Q and A type to be more efficent
-During the game, is the user presses ESC, go back to menu
-Input validation 
-Maybe add a way to add own ports based off of protocol name (with comma separated list)
-add "Keep changes" selection 


-make a way to save score?
-add correct answers: None!
"""

#Later on refactor so the question type isnt just a magic number
#Question type is what is it ASKING for
#might need answer type then so it knows how to ask it
#Q type 0 = port, 1 = tranmsission, 2 = acryonym (what is integrated in the question)
#A type 0 = port, 1 = transmission, 2 = acryonym (What is the answer?)
question1 = questionClass.portQuestion("What is the port number of ", testPorts, 2, 0)
question2 = questionClass.portQuestion("what is a transmission type of ", ports, 2, 1)
question3 = questionClass.portQuestion("What is the protocol name of the port ", testPorts, 0, 2)


#Actual startup
listOfPorts = [testPorts, ports, commonPorts]
questions = [question1, question3]
theMenu = menu.myMenu(questions, listOfPorts)
questionManager = questionMaker.qMaker(questions)

theMenu.printStarterInfo()




while True:
    
    userAnswer = theMenu.startMenu()

    #Start the game
    if (userAnswer == 0):
        questionManager.startQuestions()
        print("")
    #Print cool stuff
    elif (userAnswer == 1):
        
        optionAnswer = theMenu.printPortOptions()
        
        for q in questions:
            q.setPortList(listOfPorts[optionAnswer])

        
    #Quesetion picker selector
    elif (userAnswer == 2):
        optionAnswer = theMenu.printQuestionOptions()
        
        if (optionAnswer < len(questions)):
            questionManager.setQuestions(questions[optionAnswer])
        else:
            questionManager.setQuestions(questions)
    #Leave program
    elif (userAnswer == 3):
        theMenu.printPortInfo(testPorts)
    elif (userAnswer == 4):
        print("Goodbye.")
        raise SystemExit


#Menu Draft
"""
Welcome to port game
*Explain rules
*maybe give a little wait timer


1) 3 Questions
2) Choose question
3) Random question
4) (Eventually) port selection
5) (Eventually) question selection
6) Quit 

*During game

*After a loss 
1) Replay
2) List correct questions (with back button)
3) Back to lobby
3) Quit



"""




#refactor to where the program will NEVER ask the same question twice
#maybe how we can do it is store ports for each question so it can just look up if needed



#pop3
#snmp
#imaps
#dhcpv6Client 
#dhcpv6Server
#sips
#sip
#rdp
#ms-sql
#ldaps
#starttls
#smtps 
#ldap
#snmp-trap
#tftp
#dhcpClient
#dhcpServer
#rtcp
#pop3s
#rtp
#iscsi
#sqlnet

#http = portClass.port("HTTP", 80, "Hypertext Transport Protocol", "Web stuff")
"""
for x in range(5) 
"""
#print(http.getProtocolName())
