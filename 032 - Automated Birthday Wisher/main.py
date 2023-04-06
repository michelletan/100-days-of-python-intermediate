import datetime as dt
import random
import os
import smtplib
import pandas
import credentials
from email.message import EmailMessage

# Requirements
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person"s actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person"s email address.

CONTACTS_FILEPATH = "birthdays.csv"
TEMPLATES_DIRECTORY = "./letter_templates/"
NAME_PLACEHOLDER = "[NAME]"

sender_email = credentials.EMAIL
sender_password = credentials.APP_PASSWORD

templates = []


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


def load_templates():
    file_list = [os.path.join(TEMPLATES_DIRECTORY, f) for f in os.listdir(TEMPLATES_DIRECTORY) if os.path.isfile(
        os.path.join(TEMPLATES_DIRECTORY, f))]
    for f in file_list:
        with open(f) as file:
            template = "\n".join(file.readlines())
            templates.append(template)


def get_template() -> str:
    global templates
    if not templates:
        load_templates()
    return random.choice(templates)


def main():
    now = dt.datetime.now()

    contacts = pandas.read_csv(CONTACTS_FILEPATH)
    birthdays = contacts[(contacts.month ==
                         now.month) & (contacts.day == now.day)]

    for _, receiver in birthdays.iterrows():

        subject = "Happy Birthday!"
        message = get_template()
        message = message.replace(NAME_PLACEHOLDER, receiver["name"])
        send_email(sender_email=sender_email, sender_password=sender_password,
                   receiver_email=receiver["email"], subject=subject, message=message)


main()
