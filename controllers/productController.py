from . import app
from flask import request, render_template, redirect, url_for, Flask, jsonify, views
from models.student import product
from services.product_service import create_logic
from schemas.product_schema import ProductSchema
from werkzeug.utils import secure_filename
from flask_babel import lazy_gettext as _
from auth.auth_jwt import token_required
from auth.authentication import is_authenticated
from sqlalchemy import and_, func
import os
from . import db
import logging
logging.basicConfig(format='line no :%(lineno)d-%(message)s')
# app = Flask(__name__)

product_schema = ProductSchema()

UPLOAD_FOLDER = 'D:/study files/python/flask/curd using rest api/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class ProductView(views.MethodView):
    # @ token_required
    decorators = [is_authenticated]

    def get(self):
        try:
            # products = product.query.all()
            # product_schema = ProductSchema(many=True)
            # serilazing users i.e, converting to json() format
            name = request.args.get('name')
            pid = request.args.get('id')
            title = request.args.get('title')
            lprice = request.args.get('lprice')
            gprice = request.args.get('gprice')
            stdate = request.args.get('stdate')
            endate = request.args.get('endate')
            # print(name)
            # print(lprice, gprice)
            if name and pid and title:
                follow_up_data = product.query.filter_by(
                    pid=pid, name=name, title=title)
            elif lprice and gprice:
                print(lprice, gprice)
                follow_up_data = product.query.filter(
                    product.price >= lprice, product.price <= gprice)
            elif stdate and endate:
                print(stdate, endate)
                follow_up_data = product.query.filter(and_(func.date
                                                           (product.created_at) >= stdate, func.date(product.created_at) <= endate))
            else:
                follow_up_data = product.query.all()
            data = product_schema.dump(follow_up_data, many=True)

            response = jsonify(
                {"message": "data fetched succesfully", "data": data})
            response.status_code = 200
        except Exception as error:
            logging.exception('error in data fetching')
            response = jsonify({"message": "errror", "error": str(error)})
            response.status_code = 400
        return response

    def post(self):
        try:
            f = request.files['image']
            url = f.filename
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], url))
            # item = product(name=request.form['name'], title=request.form['title'], description=request.form['description'],
            #                price=request.form['price'], image=url)
            req_obj = {
                "name": request.form['name'],
                "title": request.form['title'],
                "description": request.form['description'],

                "price": request.form['price'],
                "image": url
            }
            item_obj = product_schema.load(req_obj)
            db.session.add(item_obj)
            db.session.commit()
            data = product_schema.dump(item_obj)
            response = jsonify(
                {"message": "data inserted succusfully", "data": data})
            response.status_code = 201
        except Exception as error:
            logging.exception('error in data inserting')
            response = jsonify(
                {"message": "error in inserting data", "error": str(error)})
            response.status_code = 400
        # print(url)
        return response

    def create():
        create_logic()
        return "table created"


class ProductDetailView(views.MethodView):
    # @ token_required
    decorators = [is_authenticated]

    def get(self, id):
        try:
            pro = product.query.filter_by(pid=id).first()
            if pro is None:
                mess = "product with name "+name+" is not found"
                response = jsonify({"message": mess})
            else:
                data = product_schema.dump(pro)
                response = jsonify(
                    {"message": "data fetched succesfully", "data": data})
                response.status_code = 200
        except Exception as error:
            logging.exception('error in data fetching')
            response = jsonify({"message": "errror", "error": str(error)})
            response.status_code = 400
        return response

    def delete(self, id):
        if request.method == "DELETE":
            try:

                print(id)
                product_delete = product.query.filter_by(pid=id).first()

                db.session.delete(product_delete)
                db.session.commit()
                data = product_schema.dump(product_delete)
                response = jsonify(
                    {"message": "data deleted succusfully", "data": data})
            except Exception as error:
                logging.exception('error in data deleting')
                response = jsonify(
                    {"message": "error in deleting data", "error": str(error)})
                response.status_code = 400
            return response

    def put(self, id):
        if request.method == "PUT":
            try:
                f = request.files['image']
                url = f.filename
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], url))
                req_obj = {
                    "name": request.form['name'],
                    "title": request.form['title'],
                    "description": request.form['description'],
                    "price": request.form['price'],
                    "image": url
                }
                product_update = product.query.filter_by(pid=id).first()
                product_object = product_schema.load(
                    req_obj, instance=product_update, partial=True)
                db.session.add(product_object)
                db.session.commit()
                data = product_schema.dump(product_object)
                response = jsonify(
                    {"message": "data updated succusfully", "data": data})
            except Exception as error:
                logging.exception('error in data editing')
                response = jsonify(
                    {"message": "error in updating data", "error": str(error)})
                response.status_code = 400
            return response
