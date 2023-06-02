import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

def get_password():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(15))
    return contrasena



def send_password(email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)

    server.starttls()
    server.login('asistencia.telovendo@gmail.com', 'shxbgahubinfkhek')
    password = get_password()
    html = f"""
    <h2 style="color:#a5e830">Contraseña:</h2>
    <label style="color:red">{password}</label>
    """
    msg = MIMEMultipart()

    msg['From'] = 'asistencia.telovendo@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Envío de Contraseña'
    content = MIMEText(html, 'html')
    msg.attach(content)
    server.send_message(msg)

    server.quit()
    return password