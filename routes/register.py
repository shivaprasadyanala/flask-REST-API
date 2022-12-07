from flask import Blueprint
from controllers.registerController import RegisterView, LoginView

reg_blueprint = Blueprint(
    'register_blueprint', __name__, url_prefix='/api/auth')

reg_blueprint.route('/post', methods=['POST'])(RegisterView.post)
reg_blueprint.route('/post', methods=['POST'])(LoginView.post)
reg_blueprint.route('/get', methods=['GET'])(LoginView.get)
# reg_blueprint.route('/create', methods=['POST'])(RegisterView.create)
