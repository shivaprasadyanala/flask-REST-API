import random
import re
from flask import request, render_template, redirect, url_for, Flask, jsonify, views
from models.student import register, db
from services.register_service import create_logic
from schemas.register_schema import RegisterSchema
import jwt
from auth.auth_jwt import token_required
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


register_schema = RegisterSchema()

app = Flask(__name__)


class RegisterView(views.MethodView):
    def post():
        try:
            if request.method == 'POST':
                register_object = register(
                    email=request.form['email'],
                    password=request.form['password'],
                    username=request.form['username']
                )

                my_email = "shivaprasadyanala@gmail.com"
                # rec_emil = "shivaprasadysp99@gmail.com"

                rec_emil = request.form['email']
                password = os.environ.get('EMAILPASS')
                symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$&@?<>~!%#"
                hasUpper = False
                hasLower = False
                hasDigit = False
                hasSpecial = False

                secpass = ""
                passwordlength = 8
                while True:
                    randpass = ""
                    for x in range(passwordlength):
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

                msg = MIMEMultipart()
                # Add Subject
                subject = "secret password for login"

                msg['Subject'] = subject

                # Add text contents
                text = "the secret password is: "+secpass
                msg.attach(MIMEText(text))
                message = msg

                with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=rec_emil,
                        msg=message.as_string()
                    )

                # print(register_object)
                user = register.query.filter_by(
                    username=register_object.username).first()
                # print(user)
                if user is None:
                    db.session.add(register_object)
                    db.session.commit()
                    data = register_schema.dump(register_object)
                    response = jsonify(
                        {"message": "data inserted succusfully", "data": data})
                else:
                    response = jsonify({"message": "user is already register"})
        except Exception as error:
            response = jsonify(
                {"message": "error while registering data", "error": str(error)})
            response.status_code = 400
        return response


# app.add_url_rule('/api/auth/register',
#                  view_func=RegisterView.as_view('post'), methods=['POST'])


def create():
    create_logic()


class LoginView(views.MethodView):
    def post2():
        try:
            if request.method == 'POST':

                username = request.form['username']
                password = request.form['password']

                user = register.query.filter_by(username=username).first()

                if user is not None:
                    if user.username == username and user.password == password:

                        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
                        ) + datetime.timedelta(minutes=30)}, 'secret_key', 'HS256')

                        response = jsonify(
                            {"message": "login succusfull", "token": token})
                    else:
                        response = jsonify(
                            {"message": "incorrect username or password"})

        except Exception as error:
            response = jsonify(
                {"message": "error while logging in", "error": str(error)})
            response.status_code = 400
        return response

    @ token_required
    def get(current_user):
        try:
            users = register.query.all()
            register_schema = RegisterSchema(many=True)
            data = register_schema.dump(users)
            response = jsonify(
                {"message": "users fetched succesfully", "data": data})
        except Exception as error:
            response = jsonify(
                {"message": "error while logging in", "error": str(error)})
            response.status_code = 400
        return response


# app.add_url_rule('/api/auth/login', view_func=LoginView.as_view('post'))
