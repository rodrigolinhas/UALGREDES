'''
TCP: is connection-oriented (os dados são transmitidos de forma confiável, usado no envio de  emails por exemplo)

Mesmo principio do UDP contudo o processo de envio é diferente:
Em vez de codificar em bytes a mensagem e declarar para que ip/porta do servidor destino
Aqui tambem é codificado em bytes CONTUDO é enviado diretamente para o servidor
E como foi dito anteriormente com o TCP não existe a perda de pacotes
'''
from socket import *

# Configurações do servidor
serverName = '10.20.71.251'                                 # IP do servidor (duh)
serverPort = 12000                                          # Port do servidor (OS PORTS TEM QUE SER IGUAIS ENTRE O client E O server)

clientSocket = socket(AF_INET, SOCK_STREAM)                 # Cria socket TCP (IPv4 + fluxo de bytes orientado a conexão)
clientSocket.connect((serverName,serverPort))               # Estabelece conexão com servidor (tudo defenido previamente)

# Mensagem que será enviada para o server
sentence = input("Input lowercase sentence:")               # Input da mensagem, nada de extraordinário
clientSocket.send(bytes(sentence, 'UTF-8'))                 # Envio direto (já conectado, DIFERENTE PARA O UDP)

modifiedSentence = clientSocket.recv(1024)                  # Recebe resposta do server (buffer até de 1024 bytes)
print ("From Server:", modifiedSentence.decode('UTF-8'))    # Recebe a mensagem, descodifica e imprime no terminal
clientSocket.close()                                        # Encerra o socket