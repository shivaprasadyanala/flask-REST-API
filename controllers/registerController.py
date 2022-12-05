from flask import request, render_template, redirect, url_for, Flask, jsonify, views
from models.student import register, db
from services.register_service import create_logic
from schemas.register_schema import RegisterSchema

register_schema = RegisterSchema()

app = Flask(__name__)


class RegisterView(views.MethodView):
    def register():
        return "register"

    def create():
        create_logic()

    def login():
        return "login"
# app.add_url_rule('/', view_func=RegisterView.as_view('index'))
