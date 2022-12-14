from settings import app, db, mail
from flask_mail import Mail, Message
import os
import random


def sendmail(email):
    email = email
    password = os.environ.get('EMAILPASS')
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$&@?<>~!%#"
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecial = False

    secpass = ""
    msg = Message('Hello', sender=os.environ.get('EMAIL_HOST_USER'),
                  recipients=[email])
    # msg.body = "Hello Flask message sent from Flask-Mail"
    while True:
        randpass = ""
        for x in range(8):
            ch = random.choice(symbols)
            # print(ch.upper(),ch.lower())
            if (ch.isupper()):
                hasUpper = True
            elif (ch.islower()):
                hasLower = True
            elif (ch.isdigit()):
                hasDigit = True
            else:
                hasSpecial = True
            randpass += ch
        if hasUpper and hasLower and hasDigit and hasSpecial:
            print(randpass)
            secpass = randpass
            break

    msg.body = "hello this is a secret key: "+secpass
    msg.subject = "secret key"
    mail.send(msg)
    print("mail sent")
