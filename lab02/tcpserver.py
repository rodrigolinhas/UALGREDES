'''
TCP: is connection-oriented (os dados são transmitidos de forma confiável, mais fiavél para emails por exemplo)

o servidor, que bonito
O mesmo objetivo do servidor UDP (enviar mensagem e receber resposta), mas com garantias de entrega ordenada e sem erros / perdas
'''
from socket import *
# Configuração do servidor
serverPort = 12000                                          # Port do servidor (OS PORTS TEM QUE SER IGUAIS ENTRE O client E O server)

serverSocket = socket(AF_INET,SOCK_STREAM)                  # Cria socket so servidor (IPv4 + fluxo de bytes orientado a conexão)
serverSocket.bind(('',serverPort))                          # Associa socket a TODAS interfaces de rede na porta (mesmo que no UDP por enquanto)

# DIFERENTE DO UDP
serverSocket.listen(1)                                      # Habilita conexões (backlog=1 → 1 conexão pendente permitida)                                      
print ('The server is ready to receive')                    # Está tudo operacional

# Loop infinito (até receber a mensagem)
while 1:
    connectionSocket, addr = serverSocket.accept()          # Aceita nova conexão
    sentence = connectionSocket.recv(1024)                  # Recebe dados da conexão estabelecida ORDENADO E SEM PERDAS (até 1024 bytes)
    capitalizedSentence = sentence.upper()                  # Modifica a mensagem / método para strings em bytes (ASCII only)
    connectionSocket.send(capitalizedSentence)              # Envio de resposta pelo mesmo canal
    connectionSocket.close()                                # Encerra conexão