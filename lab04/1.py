'''
Este codigo em Python representa enviar um email do socket TCP ao servidor SMTP 
SMTP é usado pela UALG como servidor de envio de emails.
Referencias bibliográficas usadas:
@see https://www.solarwinds.com/serv-u/tutorials/214-215-220-221-ftp-response-codes
@see https://www.ibm.com/docs/en/zos/2.4.0?topic=problems-telnet-commands-optionss
'''

from socket import *

# Mensagem a ser enviada
msg = 'I love computer networks'    # Mensagem que vai ser enviada
msgend = '\r\n.\r\n'                # IMPORTANTE PARA SIMBOLIZAR O FECHO DO CONTEUDO DO EMAIL 

# Servidor do email
mailServer = '10.10.23.49'          # IP do server
portnumber = 25                     # Porta do server (25,2525,587 são as mais usadas para os emails)

# Criacao de socket e estabelecimento de conexao TCP com servidor do email
clientSocket = socket(AF_INET, SOCK_STREAM)     # (AF_INET = IPv4 | SOCK_DGRAM = Socket TCP (orientado a conexão))
clientSocket.connect((mailServer, portnumber))  # Vai conectar ao servidor

# Analise da primeira resposta do servidor (se a conexão foi sucedivel)
recv = clientSocket.recv(1024).decode()             # Estabelece a conexão com o server
if recv[:3] != '220':                               # Se o codigo for diferente de 220 (CONEXÃO ESTABELECIDA)
    print('Erro: Servidor não respondeu com 220')   # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que foi estabelecida conexão com o server

# Envio do comando HELO para servidor (tipo uma crendencial)
heloCommand = 'HELO linhas\r\n'
clientSocket.send(heloCommand.encode())             # Envia a informação para o server
recv = clientSocket.recv(1024).decode()             # Decodifica o output do server
if recv[:3] != '250':                               # Se o codigo for diferente de 250 (UMA SUBNEGOCIAÇÃO DA OPÇÃO INDICADA.)
    print('Erro: HELO não aceite')                  # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que foi aceite a credencial


# Envio do comando MAIL FROM para servidor (email do remetente)
mailFrom = 'MAIL FROM: <a83933@ualg.pt>\r\n'
clientSocket.send(mailFrom.encode())                # Envia a informação para o server
recv = clientSocket.recv(1024).decode()             # Decodifica o output do server
if recv[:3] != '250':                               # Se o codigo for diferente de 250 (UMA SUBNEGOCIAÇÃO DA OPÇÃO INDICADA.)
    print('Erro: MAIL FROM não aceite')             # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que o email é valido

# Envio do comando RCPT TO para servidor (email do destinatario)
rcptTo = 'RCPT TO: <a83933@ualg.pt>\r\n'
clientSocket.send(rcptTo.encode())                  # Envia a informação para o server
recv = clientSocket.recv(1024).decode()             # Decodifica o output do server
if recv[:3] != '250':                               # Se o codigo for diferente de 250 (UMA SUBNEGOCIAÇÃO DA OPÇÃO INDICADA.)
    print('Erro: RCPT TO não aceite')               # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que o email é valido


# Envio do comando DATA para servidor (começo do email)
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())             # Envia a informação para o server
recv = clientSocket.recv(1024).decode()             # Decodifica o output do server
if recv[:3] != '354':                               # Se o codigo for diferente de 354 (POSSO ESCREVER O EMAIL)
    print('Erro: DATA não aceite')                  # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que posso começar a escrever o meu email

# Envio da mensagem para servidor (Escrever o conteudo do email)
clientSocket.send((msg + msgend).encode())          # Envia a informação para o server (concatenação das strings declaradas no inicio do codigo)
recv = clientSocket.recv(1024).decode()             # Decodifica o output do server
if recv[:3] != '250':                               # Se o codigo for diferente de 250 (UMA SUBNEGOCIAÇÃO DA OPÇÃO INDICADA.)
    print('Erro: Mensagem não aceite')              # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que a mensagem foi aceite e enviada para o destinatário
# NOTA: puderiamos por um assunto mas tinha que ser declarado da seguinte forma
# SUBJECT blah blah blah

# Envio do comando QUIT para servidor (fecha a conexão com o server)
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())             # Envia a informação para o server
recv = clientSocket.recv(1024).decode()             # Decodifica o output do server
if recv[:3] != '221':                               # Se o codigo for diferente de 250 (FECHOU A CONEXÃO)
    print('Erro: QUIT não aceite')                  # Mensagem de erro lol
    clientSocket.close()                            # Fecha a conexão
    exit()                                          # Sai do programa
print(recv)                                         # Imprime a mensagem que a mensagem foi fecahda a conexão

# Encerra o socket
clientSocket.close()
print('Email enviado com sucesso e ligação terminada.') # Mensagem de sucesso Yipppe!!!!