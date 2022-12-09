from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
# from routes.register import reg_blueprint
from models.student import db
from controllers.productController import ProductView


def create_app():
    # app = Flask(__name__)
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = create_app()

app.add_url_rule('/products', 'get_products', ProductView.get)
# app.add_url_rule('/products/<string:name>',
#                  'get_product_by_name', ProductView.get_by_name)
app.add_url_rule('/create', 'create_product', ProductView.create)
app.add_url_rule('/post_product', 'post_product',
                 ProductView.post, methods=['POST'])
app.add_url_rule('/delete_product/<string:id>', 'delete_product',
                 ProductView.delete, methods=['DELETE'])
app.add_url_rule('/update_product/<string:id>', 'update_product',
                 ProductView.update, methods=['PUT'])
app.register_blueprint(blueprint)
# app.register_blueprint(reg_blueprint)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
