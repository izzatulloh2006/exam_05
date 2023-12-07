import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import Celery

app = Celery('hello', broker='pyamqp://localhost:6379/0')


@app.task
def send_email():
    sender_email = "fayzullaxojaevi@gmail.com"
    sender_password = "cfuqxlwlppxdnkb"
    receiver_email = "fayzullaxojaevi@gmail.com"
    subject = "Test E-pochta"
    message = "Hello world ✅"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        text = msg.as_string()
        smtp_server.sendmail(sender_email, receiver_email, text)
        smtp_server.quit()
        print("Xabar yuborildi ✔️️")
    except Exception as e:
        print("Xabar yuborlmadi ✖️")


import smtplib
import ssl
import time

from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost/')

port = 465
smtplib_server = "smtp.gmail.com"
from_email = "fayzullaxojaevi@gmail.com"
reciever_email = input("Email kiriting : ").split()
password = "cfuqxlwlppxdnkb"
message = "Hello guys !!!"

@app.task
def hello():
    for i in reciever_email:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtplib_server, port, context=context) as server:
            server.login(from_email, password)
            time.sleep(10)
            return server.sendmail(from_email, i, message)