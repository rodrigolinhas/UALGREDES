'''
O objetivo deste lab é criar um cliente DNS
que mande uma query a um servidor de DNS
Bastou converter o UDPclient (VER LAB02)
e converter para enviar em bytes = 8 bits

consultar o seguinte site para mais detalhes: 
http://www.tcpipguide.com/free/t_DNSMessageHeaderandQuestionSectionFormat.htm#google_vignette
'''

from socket import *

# Servidor de DNS
dnsserver = '193.136.224.101'
portnumber = 53

# Criacao de DNS query
query = bytearray()

# Identification (Identificacao)
query.append(0x01) # 00000001
query.append(0x01) # 00000001

# Flags (Tipo de query)
query.append(0x00)
query.append(0x00) 

# Numero de perguntas (queremos 1 pergunta)
query.append(0x00)
query.append(0x01)

# Numero de respostas RRs
query.append(0x00)
query.append(0x00)

# Numero de authority RRs
query.append(0x00)
query.append(0x00)

# Numero de additional RRS
query.append(0x00)
query.append(0x00)

'''
Os três parametros de cima implica que é da parte do servidor DNS
que vais responder esses mesmos.
Não se torna da nossa responsabilidade de preencher tal
'''

# Pergunta
query.append(0x03)      #isto identifica quanto palavaras irá receber (nomeadamente o www)
query.append(ord('w'))
query.append(ord('w'))
query.append(ord('w'))
query.append(0x04)      #isto identifica quanto palavaras irá receber (nomeadamente o ualg)
query.append(ord('u'))
query.append(ord('a'))
query.append(ord('l'))
query.append(ord('g'))
query.append(0x02)      #isto identifica quanto palavaras irá receber (nomeadamente o pt)
query.append(ord('p'))
query.append(ord('t'))
query.append(0)         # acabou a pergunta

# A pergunta tem o tipo A (default)
query.append(0x00)
query.append(0x01)

# A pergunta tem a classe IN (internet)
query.append(0x00)
query.append(0x01)

# Abre o servidor DNS e envia a mensagem 
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(query, (dnsserver, portnumber))

# Fecha o servidor
response, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()