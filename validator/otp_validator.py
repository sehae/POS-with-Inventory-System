import random
import smtplib
import time
from email.message import EmailMessage

# Server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

from_mail = "qldbvillatura@tip.edu.ph"
app_password = "ksoa zqlm aiul wrjk"
server.login(from_mail, app_password)


# Generate OTP
def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))

    return otp


def send_otp(to_mail):
    otp = generate_otp()
    print(otp)
    otp_time = time.time()
    msg = EmailMessage()
    msg['Subject'] = 'OTP for password reset'
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg.set_content(f'Your OTP is {otp}')

    server.send_message(msg)
    print('Email Sent')

    return otp, otp_time
