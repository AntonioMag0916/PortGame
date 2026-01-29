#Port game start, 1/25/26
import portClass
import questionMaker
import random
import math

http = portClass.port("HTTP", 80, "Hypertext Transfer Protocol", "TCP","Websites, insecure", True)
https = portClass.port("HTTPS", 443, "Hypertext Transfer Protocol Secure", "TCP", "Websites, secure", True)
smtp = portClass.port("SMTP", 25, "Simple Mail Transfer Protocl", "TCP", "Mail deilvery protocol", True)
telnet = portClass.port("Telnet", 23, "Telent", "TCP", "Remote access protocol, insecure", False)
ssh = portClass.port("SSH", 22, "Secure Shell", "TCP/UDP", "Remote access protocol, secure", True)
dns = portClass.port("DNS", 53, "Domain Name System", "TCP/UDP", "IPs to human readable text", True)
mysql = portClass.port("MySQL", 3306, "MySQL", "TCP", "SQL Server", False)
ftpdata = portClass.port("FTP-Data", 20, "FTP-Data", "TCP/UDP", "FTP download and upload service", False)
ftp = portClass.port("FTP", 21, "File Transfer Protocol", "TCP/UDP", "Allows for a stateful channel for FTP commands", True)
syslog = portClass.port("Syslog", 514, "System Logging", "UDP", "Enables centralized collection of logs and events", True)
ntp = portClass.port("NTP", 123, "Network Time Protocol", "UDP", "Automatic time update protocol", True)

ports = [http, https, smtp, telnet, ssh, dns, mysql, ftpdata, ftp, syslog, ntp]

question1 = questionMaker.question("What is the port number of ", ports)
question2 = questionMaker.question("what is the transmission type of ", ports)
question3 = questionMaker.question("what is the acronym of the port num ", ports)

portsLen = len(ports)

#amountTracker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

questions = ["What is the port number of ", "what is the transmission type of ", "what is the acronym of the port num "]
tempQuestions = ["What is the port number of "]
questionManager = questionMaker.qMaker(tempQuestions)

questionManager.randomQuestion()

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
