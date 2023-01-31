#!/usr/bin/env python

import os
import smtplib

SES_SMTP_HOST = "email-smtp.us-east-1.amazonaws.com" # 'localhost'
SES_SMTP_USERNAME = os.getenv('SES_SMTP_USERNAME')
SES_SMTP_PASSWORD = os.getenv('SES_SMTP_PASSWORD')


def send_email(sender, receivers, message):
    try:
        smtp = smtplib.SMTP(SES_SMTP_HOST)
        smtp.starttls()
        smtp.login(SES_SMTP_USERNAME, SES_SMTP_PASSWORD)
        print(smtp.local_hostname)
        smtp.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print("Error: unable to send email")
        print(e)


if __name__ == "__main__":
    sender = 'harikrishnan.b@inapp.com'
    receivers = ['harikrishnan.b@inapp.com']
    message = f"""From: From Person <{sender}>
    To: To Person <{receivers[0]}>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """
    send_email(sender, receivers, message)