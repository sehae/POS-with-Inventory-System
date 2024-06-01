import random
import smtplib
from email.message import EmailMessage

# Generate OTP
otp = ""
for i in range(6):
    otp += str(random.randint(0, 9))

print(otp)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

from_mail = "qldbvillatura@tip.edu.ph"
app_password = "ksoa zqlm aiul wrjk"
server.login(from_mail, app_password)
to_mail = input("Enter your email: ")

msg = EmailMessage()
msg['Subject'] = 'OTP for password reset'
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content(f'Your OTP is {otp}')

server.send_message(msg)
print('Email Sent')
