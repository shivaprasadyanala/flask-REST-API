from flask_marshmallow import Marshmallow
from flask import Flask
app = Flask(__name__)
ma = Marshmallow(app)


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "age", "location", "_links")

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("blueprint.index"),
            "collection": ma.URLFor("blueprint.index")}
    )
