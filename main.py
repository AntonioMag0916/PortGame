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



ftpdata = portClass.port("FTP-DATA", 20, "File Transfer Protocol-Data", "TCP/UDP", "FTP download and upload service")
ftpcon = portClass.port("FTP-CONTROL", 21, "File Transfer Protocol-Control", "TCP/UDP", "Allows for a stateful channel for FTP commands")
ssh = portClass.port("SSH", 22, "Secure Shell", "TCP/UDP", "Remote access protocol, secure")
telnet = portClass.port("TELNET", 23, "Telent", "TCP", "Remote access protocol, insecure")
smtp = portClass.port("SMTP", 25, "Simple Mail Transfer Protocl", "TCP", "Mail deilvery protocol")
tacacs = portClass.port("TACACS", 49, "TACACS", "TCP", "N/A")
dns = portClass.port("DNS", 53, "Domain Name System", "TCP/UDP", "IPs to human readable text")
dhcpserver = portClass.port("DHCP-SERVER", 67, "DHCP-SERVER", "UDP", "N/A")
dhcpclient = portClass.port("DHCP-CLIENT", 68, "DHCP-CLIENT", "UDP", "N/A")
tftp = portClass.port("TFTP", 69, "Trivial File Transfer Protocol", "UDP", "N/A")
http = portClass.port("HTTP", 80, "Hypertext Transfer Protocol", "TCP","Website communication, insecure")
kerberos = portClass.port("KERBEROS", 88, "Kerberos", "TCP/UDP", "N/A")
pop3 = portClass.port("POP3", 110, "Post Office Protocol", "TCP", "N/A")
nntp = portClass.port("NNTP", 119, "Network News Transfer Protocol", "TCP", "N/A")
ntp = portClass.port("NTP", 123, "Network Time Protocol", "UDP", "Automatic time update protocol")
rpc = portClass.port("RPC", 135, "Remove Procedure Protocol", "TCP", "N/A")
netbiosName = portClass.port("NETBIOS-NAME", 137, "NETBIOS-NAME", "UDP", "N/A")
netbiosDatagram = portClass.port("NETBIOS-DATAGRAM", 138, "NETBIOS-DATAGRAM", "UDP", "N/A")
netbiosSession = portClass.port("NETBIOS-SESSION", 139, "NETBIOS-SESSION", "TCP", "N/A")
imap = portClass.port("IMAP", 143, "Internet Message Access Protocol", "TCP", "N/A")
snmp = portClass.port("SNMP", 161,"Simple Network Management Protocol", "TCP/UDP", "Used to centrally collect and organize data from other network devices")
snmptrap = portClass.port("SNMP-TRAP", 162 ,"Simple Network Management Protocol - Trap", "TCP/UDP", "Unsolicited message from Agent to Manager ")
xdmcp = portClass.port("XDMCP", 177, "X Display Manager Control Protocol", "UDP", "N/A")
bgp = portClass.port("BGP", 179, "Border Gateway Protocol", "TCP", "N/A")
irc = portClass.port("IRC", 194, "Internet Relay Chat", "TCP", "N/A")
ldap = portClass.port("LDAP", 389, "Lightweight Directory Access Protocol", "TCP/UDP", "AD Protocol")
https = portClass.port("HTTPS", 443, "Hypertext Transfer Protocol Secure", "TCP", "Website communication, secure")
smb = portClass.port("SMB", 445, "Server Message Block", "TCP", "Network file sharing protocol")
smtps = portClass.port("SMTPS", 465, "Simple Mail Transfer Protocol Secure", "TCP", "Implicit TLS")
ipsec = portClass.port("IPSEC", 500, "Internet Key Exchange", "UDP", "Used with IKE")
syslog = portClass.port("SYSLOG", 514, "System Logging", "UDP", "Enables centralized collection of logs and events")
starttls = portClass.port("STARTTLS", 587, "STARTTLS", "TCP", "SMTP submission, better than smtps")
ldaps = portClass.port("LDAPS", 636, "LDAP Secure", "TCP", "N/A")
imaps = portClass.port("IMAPS", 993, "IMAP Secure", "TCP", "N/A")
pop3s = portClass.port("POP3S", 995, "POP3 Secure", "TCP", "N/A")
mssqlserver = portClass.port("MS-SQL-Server", 1433, "MS-SQL-Server", "TCP", "N/A")
mssqlbrowser = portClass.port("MS-SQL-Browser", 1434, "MS-SQL-Browser", "UDP", "N/A")
oracleDB = portClass.port("ORACLE-DB", 1521, "ORACLE-DB", "TCP", "Targeted port by attackers")
l2tp = portClass.port("L2TP", 1701, "Layer 2 Tunneling Protocol", "UDP", "N/A")
pptp = portClass.port("PPTP", 1723, "Point to Point Protocol", "TCP", "N/A")
radiusAuth = portClass.port("RADIUS-AUTH", 1812, "RADIUS-AUTH", "UDP", "N/A")
radiusAccounting = portClass.port("RADIUS-ACCOUNTING", 1813, "RADIUS-ACCOUNTING", "UDP", "N/A")
nfs = portClass.port("NFS", 2049, "Network File System", "TCP/UDP", "N/A")
squidProxy = portClass.port("SQUID-PROXY", 3128, "SQUID-PROXY", "TCP", "N/A")
mysql = portClass.port("MYSQL", 3306, "MySQL", "TCP", "SQL Server")
rdp = portClass.port("RDP", 3389, "Remote Desktop Protocol", "TCP", "Remote access")
metasploit = portClass.port("METASPLOIT", 4444, "METASPLOIT", "TCP", "N/A")
sip = portClass.port("SIP", 5060, "Session Initation Protocol", "TCP/UDP", "N/A")
sips = portClass.port("SIPS", 5061, "SIP Secure", "TCP/UDP", "N/A")
postgreSQL = portClass.port("POSTGRE-SQL", 5432, "POSTGRE-SQL", "TCP", "N/A")
vnc = portClass.port("VNC", 5900, "Virtual Network Computing", "TCP", "N/A")
syslogTLS = portClass.port("SYSLOG-TLS", 6514, "Secure Syslog", "TCP", "N/A")
httpAltProxy = portClass.port("HTTP-ALT-PROXY", 8080, "HTTP Alternative", "TCP", "N/A")
httpAltVPN = portClass.port("HTTP-ALT-PROXY", 8443, "HTTP Alternative", "TCP", "N/A")

allPorts = [ftpdata, ftpcon, ssh, telnet, smtp, tacacs, dns, 
            dhcpserver, dhcpclient, tftp, http, kerberos, pop3, 
            nntp, ntp, rpc, netbiosName, netbiosDatagram, netbiosSession, 
            imap, snmp, snmptrap, xdmcp, bgp, irc, ldap, https, smb, 
            smtps, ipsec, syslog, starttls, ldaps, imaps, pop3s, mssqlserver, 
            mssqlbrowser, oracleDB, l2tp, pptp, radiusAuth, radiusAccounting,
            nfs, squidProxy, mysql, rdp, metasploit, sip, sips,
            postgreSQL, vnc, syslogTLS, httpAltProxy, httpAltVPN]

ports = [http, https, smtp, telnet, ssh, dns, mysql, ftpdata, ftpcon, syslog, ntp]
testPorts = [http, dns, ntp]
commonPorts = [http, https, ssh, dns, ntp, smtp, smb, telnet] #Startoff with 8
#Think of more port lists
secPlusMain = [ftpdata, ftpcon, ssh, telnet, smtp, tacacs, dns, http, pop3, imap, snmp, snmptrap, ldap, https, smb, ipsec, ldaps, pop3s, imaps, l2tp, pptp, radiusAuth, radiusAccounting, rdp, vnc]

secPlusPortsPlus = [ftpdata, ftpcon, ssh, telnet, smtp, tacacs, dns, http, kerberos, 
                    pop3, imap, snmp, snmptrap, bgp, ldap, https, smb, ipsec, ldaps, pop3s, 
                    imaps, l2tp, pptp, radiusAuth, radiusAccounting, rdp, sip, sips, vnc, syslogTLS]

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
question1 = questionClass.portQuestion("What is the port number of ", secPlusMain, 2, 0)
question2 = questionClass.portQuestion("what is a transmission type of ", secPlusMain, 2, 1)
question3 = questionClass.portQuestion("What is the protocol name of the port ", secPlusMain, 0, 2)


#Actual startup
listOfPorts = [secPlusMain, secPlusPortsPlus, allPorts]
questions = [question1, question2, question3]
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
        
        theMenu.printPortInfo(allPorts)
        
        #Change this later but this should grab whatever list of ports is currently here 

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
