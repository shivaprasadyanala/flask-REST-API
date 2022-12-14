from . import app
from utils import sendmail
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


class RegisterView(views.MethodView):
    def post():
        try:

            register_object = register(
                email=request.form['email'],
                password=request.form['password'],
                username=request.form['username']
            )

            rec_emil = request.form['email']
            sendmail(rec_emil)
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
