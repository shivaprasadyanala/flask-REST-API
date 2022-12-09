from controllers.productController import ProductView

from ..app import app
from flask import Flask
app = Flask(__name__)
print("hi in product")
app.add_url_rule('/product', 'product', ProductView.get_product)
