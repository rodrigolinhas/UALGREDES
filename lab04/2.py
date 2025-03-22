'''
Este codigo em Python representa enviar um email através do servidor SMTP do outlook (office 365)
SMTP é usado pela UALG como servidor de envio de emails.
A estrutura do codigo será completamente diferente do anterior uma vez que é uma conexão direta com o SMTP, tornando-se assim mais rapido
Contudo precisamos de introduzir credencias e ser mais expecificos na formatação de envio
'''

import smtplib

#declarar a o servidor
SMTP_SERVER = 'smtp.office365.com'          # IP do server
SMTP_PORT = 587                             # Port do server

sender = 'a83933@ualg.pt'                   # Email do remetente
password = ""                               # Password do remetente (claro que não vou por a minha pass aqui lol)
recipient = 'a83933@ualg.pt'                # Email do destinatário
subject = 'teste'                           # Assunto do email
body = 'blah blah blah.'                    # O email em si (NOTA: só se mete o . quando a mensagem acaba)

#headers (Servem para defenir a informação)
headers = [
    "From: " + sender,                      # Define o remetente.
    "Subject: " + subject,                  # Define o assunto do email.
    "To: " + recipient                      # Define o destinatário.
]
headers = "\r\n".join(headers)              # Junta os headers usando o \r\n que é obrigatorio no SMTP.

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)                      # Cria a conexão com o servidor SMTP
session.ehlo()                                                      # Identificaçar que somos um remetente compatível com o protocolo SMTP (equivalente ao HELO).
session.starttls()                                                  # Inicia uma conexão encriptada (TLS) entre o remetente e o servidor.
session.ehlo()                                                      # Faz se de novo isto para reafirmar nossa identidade após ativar o TLS.
session.login(sender, password)                                     # Faz o login
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)    # Envia o email
session.quit()                                                      # Fecha a coenxão
print('Email enviado com sucesso e ligação terminada.')             # Mensagem de sucesso Yipppe!!!!