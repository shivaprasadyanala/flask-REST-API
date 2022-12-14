from settings import app, db, mail
from flask_mail import Mail, Message
import os
import random
from random import choice, shuffle
import json
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password():
    """
    Generate random password.
    """
    pwd = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits)] \
        + [choice(ascii_lowercase + ascii_uppercase + digits)
           for _ in range(5)]
    shuffle(pwd)
    pwd = ''.join(pwd)
    return pwd


def sendmail(email):
    email = email
    password = os.environ.get('EMAILPASS')
    msg = Message('Hello', sender=os.environ.get('EMAIL_HOST_USER'),
                  recipients=[email])
    # symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$&@?<>~!%#"
    # hasUpper = False
    # hasLower = False
    # hasDigit = False
    # hasSpecial = False

    # secpass = ""

    # # msg.body = "Hello Flask message sent from Flask-Mail"
    # while True:
    #     randpass = ""
    #     for x in range(8):
    #         ch = random.choice(symbols)
    #         # print(ch.upper(),ch.lower())
    #         if (ch.isupper()):
    #             hasUpper = True
    #         elif (ch.islower()):
    #             hasLower = True
    #         elif (ch.isdigit()):
    #             hasDigit = True
    #         else:
    #             hasSpecial = True
    #         randpass += ch
    #     if hasUpper and hasLower and hasDigit and hasSpecial:
    #         print(randpass)
    #         secpass = randpass
    #         break
    secret_password = get_random_password()
    print(secret_password)
    msg.body = "hello this is a secret key: "+secret_password
    msg.subject = "secret key"
    mail.send(msg)
    print("mail sent")
