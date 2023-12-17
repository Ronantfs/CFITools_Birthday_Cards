import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import constants
from typing import List, Tuple
import os


def compile_email(list_of_message_tuples: List[Tuple[str, ...]]):
    email_body ="Birthday's this week:"

    for message_tuple in list_of_message_tuples:
        name = message_tuple[0]
        birthday = message_tuple[1]
        phone_number = message_tuple[2]
        message = message_tuple[3]

        # Format and add the current message to the email body
        email_body += "\n"
        email_body += f"Name: {name}\n"
        email_body += f"Birthday: {birthday}\n"
        email_body += f"Phone Number: TODO \n"
        email_body += f"Message: {message}\n"
        email_body += "\n"
        email_body += "------------------------"

    return email_body


def send_email(subject: str, body: str, image_paths: List[str]):
    # Email credentials
    sender_email = constants.sender_email
    receiver_email = constants.adam_email
    password = constants.google_app_pw

    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Attach images
    for path in image_paths:
        with open(path, 'rb') as file:
            img = MIMEImage(file.read())
            img.add_header('Content-Disposition', 'attachment', filename=path)
            message.attach(img)

    # Send the email
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_email, password)
        text = message.as_string()
        session.sendmail(sender_email, receiver_email, text)
        session.quit()
        print("Mail Sent Successfully")
    except Exception as e:
        print(f"Error: {e}")