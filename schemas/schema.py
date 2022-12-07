from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask import Flask
from models.student import student, db
from marshmallow import fields
app = Flask(__name__)
ma = Marshmallow(app)


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "name", "age", "location", "_links")
        model = student
        sqla_session = db.Session
        include_fk = True
        load_instance = True

        # sqla_session = db
    # id = fields.Integer(dump_only=True)
    # name = fields.String(require=True)
    # age = fields.Integer(dump_only=True)
    # location = fields.String(require=True)
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("blueprint.get"),
            "collection": ma.URLFor("blueprint.get")}
    )
