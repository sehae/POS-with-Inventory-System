from email.message import EmailMessage
from server.email_server import server, from_mail


def send_username_password(username, password, email):
    msg = EmailMessage()
    msg['Subject'] = 'MOON HEY HOTPOT - WELCOME TO THE TEAM!'
    msg['From'] = from_mail
    msg['To'] = email

    message = f"""
    Hello,

    Here are your login details:

    Username: {username}
    Password: {password}

    Please do not share these details with anyone. You are free to change your password once you log in.

    Best,
    Moon Hey Hotpot and Grill Team
    """

    msg.set_content(message)

    server.send_message(msg)

    print('Email Sent')