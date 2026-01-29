#Port game start, 1/25/26
import portClass

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


for x in ports:
    print(x.getAcronym())



#ftpClient
#ftpServer
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
#mysql
#rtcp
#pop3s
#rtp
#iscsi
#sqlnet

#http = portClass.port("HTTP", 80, "Hypertext Transport Protocol", "Web stuff")

#print(http.getAcronym())
