from flask import Blueprint
from controllers.studentController import StudentView


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(StudentView.index)
blueprint.route('/create', methods=['GET'])(StudentView.create)
blueprint.route('/insert', methods=['POST'])(StudentView.insert)
blueprint.route('/delete/<string:id>', methods=['GET'])(StudentView.delete)
blueprint.route('/update/<string:id>', methods=['POST'])(StudentView.update)
