from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def prepara_email(texto, email):
    msg = MIMEMultipart()
    msg['from'] = 'Tiago'
    msg['to'] = email
    msg['subject'] = 'NOTAS UNIVERSIDADE'
    msg.attach(MIMEText(texto))
    return msg


def envia_email(texto, email, senha):
    msg = prepara_email(texto, email)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)
        print('Email enviado.')
