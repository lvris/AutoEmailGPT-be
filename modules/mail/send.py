import settings

from markdown2 import markdown
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def connect_to_smtp(smtp_server, smtp_port, username, password):
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(username, password)
    return server

def create_mail(server, to_addr, subject, markdown_text):
    message = MIMEMultipart()
    message['From'] = server.user
    message['To'] = to_addr
    message['Subject'] = subject

    html_content = markdown(markdown_text, extras=["fenced-code-blocks"])
    message.attach(MIMEText(html_content, 'html'))
    
    server.send_message(message)

if __name__ == "__main__":
    server = connect_to_smtp(
        settings.smtp_server, 
        settings.smtp_port, 
        settings.username, 
        settings.password
    )
    create_mail(server, settings.username, "Hello, World")
