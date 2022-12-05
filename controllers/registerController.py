from flask import request, render_template, redirect, url_for, Flask, jsonify, views
from models.student import register, db
from services.register_service import create_logic
from schemas.register_schema import RegisterSchema

register_schema = RegisterSchema()

app = Flask(__name__)


class RegisterView(views.MethodView):
    def register():
        try:
            if request.method == 'POST':
                uname = request.form['username']
                password = request.form['password']
                email = request.form['email']
                db.execute('insert into register(email,password,username) values (%s,%s,%s)', (
                    uname, password, email,))
        except Exception as error:
            response = jsonify(
                {"message": "error while registering data", "error": str(error)})
            response.status_code = 400

    def create():
        create_logic()

    def login():
        return "login"
# app.add_url_rule('/', view_func=RegisterView.as_view('index'))
