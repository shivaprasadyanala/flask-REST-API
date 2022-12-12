from controllers.productController import ProductView, ProductDetailView

from . import app
app.add_url_rule(
    '/products', view_func=ProductView.as_view('get_products'))
app.add_url_rule(
    '/products/<id>', view_func=ProductDetailView.as_view('put_products'))
