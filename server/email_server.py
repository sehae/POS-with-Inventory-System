import smtplib

# Server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

from_mail = "qldbvillatura@tip.edu.ph"
app_password = "ksoa zqlm aiul wrjk"
server.login(from_mail, app_password)