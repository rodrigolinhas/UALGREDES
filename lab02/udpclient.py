'''
UDP: no “connection” between client and server 
(os dados transmitidos podem receber fora de ordem ou pode-se perder, muito usado em servicos de trafego de voz)

A premissa é simples, declaro o ip e o port do servidor de destino
depois escrevo a mensagem desejada, a mesma será enviada codificada em bytes
Após a conexao sucessível, será retornado a mensagem recebida do server
e é fechado o socket do cliente
'''
from socket import *

# Configurações do servidor
serverName = 'ip do servidor fica aqui'                                 # IP do servidor (duh)
serverPort = 12000                                                      # Port do servidor (OS PORTS TEM QUE SER IGUAIS ENTRE O client E O server)

# Cria o socket do cliente
clientSocket = socket(AF_INET, SOCK_DGRAM)                              # (AF_INET = IPv4 | SOCK_DGRAM = Socket UDP (não orientado a conexão))

# Mensagem que será enviada para o server
message = input("Input lowercase sentence:")                            # Input da mensagem, nada de especial
clientSocket.sendto(bytes(message, 'UTF-8'),(serverName, serverPort))   # Envia a mensagem codificada em bytes para o servidor, especificando o mesmo
                                                                        # NOTA: UTF-8 garante codificação padrão para caracteres especiais
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)            # Aguarda a resposta do servidor (buffer de até 2048 bytes)
                                                                        # NOTA: que é declarado aqui o serverAddres (mas não é utlizado?) 
print ("From server:",modifiedMessage.decode('UTF-8'))                  # Recebe a mensagem, descodifica e imprime no terminal
clientSocket.close()                                                    # Encerra o socket