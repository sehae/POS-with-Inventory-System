import smtplib

from_mail = "qldbvillatura@tip.edu.ph"
app_password = "ksoa zqlm aiul wrjk"

def get_smtp_server():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_mail, app_password)
    return server
