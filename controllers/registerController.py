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
                register_object = register(
                    email=request.form['email'],
                    password=request.form['password'],
                    username=request.form['username']
                )
                print(register_object)
                user = register.query.filter_by(
                    username=register_object.username).first()
                print(user)
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

    def create():
        create_logic()

    def login():
        try:
            if request.method == 'POST':

                username = request.form['username']
                password = request.form['password']

                user = register.query.filter_by(username=username).first()
                print(user)
                if user is not None:
                    if user.username == username and user.password == password:
                        response = jsonify({"message": "login succusfull"})
                    else:
                        response = jsonify(
                            {"message": "incorrect username or password"})

        except Exception as error:
            response = jsonify(
                {"message": "error while logging in", "error": str(error)})
            response.status_code = 400
        return response
# app.add_url_rule('/', view_func=RegisterView.as_view('index'))
