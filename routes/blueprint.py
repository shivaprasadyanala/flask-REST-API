from flask import Blueprint
from controllers.studentController import StudentView


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/get', methods=['GET'])(StudentView.get)
# blueprint.route('/create', methods=['GET'])(StudentView.create)
blueprint.route('/post', methods=['POST'])(StudentView.post)
blueprint.route('/delete/<string:id>', methods=['DELETE'])(StudentView.delete)
blueprint.route('/put/<string:id>', methods=['PUT'])(StudentView.put)
