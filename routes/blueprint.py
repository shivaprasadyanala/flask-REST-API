from flask import Blueprint
from controllers.studentController import index, create, insert, delete, update


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['POST'])(insert)
blueprint.route('/delete/<string:id>', methods=['GET'])(delete)
blueprint.route('/update/<string:id>', methods=['POST'])(update)
