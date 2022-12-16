from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask import Flask
from marshmallow import fields, validate
from models.student import register, db
from . import app
ma = Marshmallow(app)


class RegisterSchema(SQLAlchemyAutoSchema):
    username = fields.Str(required=True, validate=[
        validate.Length(min=4, max=250)])
    email = fields.Str(required=True, validate=[
        validate.Length(min=5, max=250)])
    password = fields.Str(required=True, validate=[
        validate.Length(min=8)])

    class Meta:
        fields = ("id", "email", "username", "password", "_links")
        # exclude = ("password")
        model = register
        sqla_session = db.Session
        include_fk = True
        load_instance = True

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("register_user"),
            "collection": ma.URLFor("register_user")}
    )
