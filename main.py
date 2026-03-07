#Port game start, 1/25/26
import portClass
import questionMaker
import questionClass




http = portClass.port("HTTP", 80, "Hypertext Transfer Protocol", "TCP","Websites, insecure", True)
https = portClass.port("HTTPS", 443, "Hypertext Transfer Protocol Secure", "TCP", "Websites, secure", True)
smtp = portClass.port("SMTP", 25, "Simple Mail Transfer Protocl", "TCP", "Mail deilvery protocol", True)
telnet = portClass.port("TELNET", 23, "Telent", "TCP", "Remote access protocol, insecure", False)
ssh = portClass.port("SSH", 22, "Secure Shell", "TCP/UDP", "Remote access protocol, secure", True)
dns = portClass.port("DNS", 53, "Domain Name System", "TCP/UDP", "IPs to human readable text", True)
mysql = portClass.port("MYSQL", 3306, "MySQL", "TCP", "SQL Server", False)
ftpdata = portClass.port("FTP-DATA", 20, "FTP-Data", "TCP/UDP", "FTP download and upload service", False)
ftpcon = portClass.port("FTP-CON", 21, "File Transfer Protocol", "TCP/UDP", "Allows for a stateful channel for FTP commands", True)
syslog = portClass.port("SYSLOG", 514, "System Logging", "UDP", "Enables centralized collection of logs and events", True)
ntp = portClass.port("NTP", 123, "Network Time Protocol", "UDP", "Automatic time update protocol", True)

ports = [http, https, smtp, telnet, ssh, dns, mysql, ftpdata, ftpcon, syslog, ntp]
testPorts = [http, dns, ntp]
"""
---Needed Updates---
-maybe for occurences like ftp, make it to where there can be multiple ports under the same protocol or display how to type in ftp-data/con
-maybe have a class that handles the menu flow and display text (like saying ftp-con vs ftp-data)
-Make a menu where you can choose if you want to do random questions or a select question
-Refactor Q and A type to be more efficent
-Either create a new class for questionMaker that will only use a single question and not rotate out
-,or have a variable in the constructor that will choose which function to use
-If there are no ports for a question, do not choose it (if we are using random)
-Tell the user that when they get one wrong they will end the program (ask if they want to start over maybe)
-Input validation 
-Add a way for the user to put TCP/UDP or TCP or UDP for a port that has both TCP/UDP (reword question too )

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
question3 = questionClass.portQuestion("what is the acronym of the port num ", testPorts, 0, 2)


questions = [question1, question3]
questionManager = questionMaker.qMaker(questions)


questionManager.startQuestions()

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
#print(http.getAcronym())
