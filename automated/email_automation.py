from email.message import EmailMessage

from server.email_server import from_mail, get_smtp_server


# Account Creation
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

    # Get a new SMTP connection
    server = get_smtp_server()

    server.send_message(msg)

    print('Email Sent')

    server.quit()


# Account Update
def send_new_details(username, email):
    msg = EmailMessage()
    msg['Subject'] = 'MOON HEY HOTPOT - WE HAVE UPDATED YOUR LOGIN DETAILS!'
    msg['From'] = from_mail
    msg['To'] = email

    message = f"""
    Hello,

    We have updated your login details, here are your new login details:

    Username: {username}
    Password: still the same as your previous password.

    Disregard the previous login details, they are no longer valid.
    Please do not share these details with anyone. You are free to change your password once you log in.

    Best,
    Moon Hey Hotpot and Grill Team
    """

    # Get a new SMTP connection
    server = get_smtp_server()

    msg.set_content(message)
    server.send_message(msg)
    print('Email Sent')

    server.quit()
