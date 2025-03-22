'''
UDP: no “connection” between client and server 
(os dados transmitidos podem receber fora de ordem ou pode-se perder)

o servidor, aonde a magia acontece
Tem um loop infinito para receber as mensagems dos clientes
Dentro do loop, quando ele recebe a mensagem do cliente ele modifica (neste caso deixa em caps-lock)
e por fim manda de volta para o cliente
'''
from socket import *

# Configurações do servidor
serverPort = 12000                                          # Port do servidor (OS PORTS TEM QUE SER IGUAIS ENTRE O client E O server)
serverSocket = socket(AF_INET, SOCK_DGRAM)                  # Cria o socket do servidor

serverSocket.bind(("", serverPort))                         # Vincula socket a TODAS interfaces na porta especificada
print ("The server is ready to receive")                    # Está tudo operacional

# Loop infinito (para receber as mensagens)
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)    # Recebe mensagem + endereço do cliente (buffer de até 2048 bytes)
    modifiedMessage = message.upper()                       # Modifica a mensagem / método para strings em bytes (ASCII only)
    serverSocket.sendto(modifiedMessage, clientAddress)     # Retorna a mensagem para o cliente