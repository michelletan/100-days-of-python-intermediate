import smtplib
from email.message import EmailMessage


def get_smtp_server(host: str) -> str:
    if "@yahoo." in host:
        return "smtp.mail.yahoo.com"
    elif "@gmail." in host:
        return "smtp.gmail.com"
    elif "@hotmail." in host or "@live." in host:
        return "smtp.live.com"


def send_email(sender_email: str, sender_password: str, receiver_email: str, subject: str, message: str):
    with smtplib.SMTP_SSL(get_smtp_server(sender_email)) as connection:
        connection.login(user=sender_email, password=sender_password)

        mail = EmailMessage()
        mail["Subject"] = subject
        mail["From"] = sender_email
        mail["To"] = receiver_email
        mail.set_content(message)
        connection.send_message(mail)
