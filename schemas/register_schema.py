from flask_marshmallow import Marshmallow
from flask import Flask
app = Flask(__name__)
ma = Marshmallow(app)


class RegisterSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password", "username", "_links")

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("student.index"),
            "collection": ma.URLFor("student.index")}
    )
