# from flask import Blueprint
from controllers.registerController import RegisterView, LoginView

# reg_blueprint = Blueprint(
#     'register_blueprint', __name__, url_prefix='/api/auth')

# reg_blueprint.route('/register', methods=['POST'])(RegisterView.post)
# reg_blueprint.route('/login', methods=['POST'])(LoginView.post2)
# reg_blueprint.route('/getusers', methods=['GET'])(LoginView.get)
# reg_blueprint.route('/create', methods=['POST'])(RegisterView.create)
from . import app
app.add_url_rule(
    '/api/auth/register', view_func=RegisterView.as_view('register_user'))
app.add_url_rule(
    '/api/auth/login', view_func=LoginView.as_view('login_user'))
