from flask_marshmallow import Marshmallow
from flask import Flask
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.student import product, db
app = Flask(__name__)
ma = Marshmallow(app)


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        fields = ("pid", "name", "title", "description", "price",
                  "image", "created_at", "updated_at", "_links")
        model = product
        sqla_session = db.Session
        include_fk = True
        load_instance = True
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("get_products"),
            "collection": ma.URLFor("get_products")}
    )
