from socket import *

# Servidor de DNS
dnsserver = '192.168.1.137'
portnumber = 53

# Criacao de DNS query
query = bytearray()

# Identification
query.append(0x01)
query.append(0x01)

# Flags
query.append(0x01)
query.append(0x00)

# Number of Questions
query.append(0x00)
query.append(0x01)

# Number of Answers RRs
query.append(0x00)
query.append(0x00)

#Number of authority RRs
query.append(0x00)
query.append(0x00)

# Number of additional RRS
query.append(0x00)
query.append(0x00)

# Number of Questions
query.append(0x03)
query.append(ord('w'))
query.append(ord('w'))
query.append(ord('w'))
query.append(0x04)
query.append(ord('u'))
query.append(ord('a'))
query.append(ord('l'))
query.append(ord('g'))
query.append(0x02)
query.append(ord('p'))
query.append(ord('t'))
query.append(0)

# Question Type 'A'
query.append(0x00)
query.append(0x01)

# Question Class 'IN'
query.append(0x00)
query.append(0x01)

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(query, (dnsserver, portnumber))

# Close Server
response, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()
