from . import app
from flask_marshmallow import Marshmallow
from flask import Flask
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from models.student import product, db
ma = Marshmallow(app)


class ProductSchema(SQLAlchemyAutoSchema):
    name = fields.Str(required=True, validate=[
                      validate.Length(min=4, max=250)])
    title = fields.Str(required=True, validate=[
        validate.Length(min=5, max=250)])
    description = fields.Str(required=True, validate=[
        validate.Length(min=10)])
    price = fields.Str(required=True, validate=[
        validate.Length(min=5, max=100)])
    image = fields.Str(required=True)

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
