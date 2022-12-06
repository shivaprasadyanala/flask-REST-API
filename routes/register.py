from flask import Blueprint
from controllers.registerController import RegisterView

reg_blueprint = Blueprint(
    'register_blueprint', __name__, url_prefix='/api/auth')

reg_blueprint.route('/register', methods=['POST'])(RegisterView.register)
reg_blueprint.route('/login', methods=['POST'])(RegisterView.login)
reg_blueprint.route('/users', methods=['GET'])(RegisterView.get_all_users)
# reg_blueprint.route('/create', methods=['POST'])(RegisterView.create)
