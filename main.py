#Port game start, 1/25/26
import portClass



http = portClass.port("HTTP", 80, "Hypertext Transfer Protocol", "TCP","Websites, insecure", True)
https = portClass.port("HTTPS", 443, "Hypertext Transfer Protocol Secure", "TCP", "Websites, secure", True)
smtp = portClass.port("SMTP", 25, "Simple Mail Transfer Protocl", "TCP", "Mail deilvery protocol", True)
telnet = portClass.port("Telnet")

#ftpClient
#ftpServer
#ssh
#telnet
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
#syslog
#ldap
#snmp-trap
#ntp
#tftp
#dhcpClient
#dhcpServer
#dns
#mysql
#rtcp
#pop3s
#rtp
#iscsi
#sqlnet

#http = portClass.port("HTTP", 80, "Hypertext Transport Protocol", "Web stuff")

#print(http.getAcronym())
