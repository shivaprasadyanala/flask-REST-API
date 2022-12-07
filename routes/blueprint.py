from flask import Blueprint
from controllers.studentController import StudentView


blueprint = Blueprint('student', __name__, url_prefix='/api/student')

blueprint.route('/', methods=['GET'])(StudentView.get)
# blueprint.route('/create', methods=['GET'])(StudentView.create)
blueprint.route('/insert', methods=['POST'])(StudentView.post)
blueprint.route('/delete/<string:id>', methods=['GET'])(StudentView.delete)
blueprint.route('/update/<string:id>', methods=['POST'])(StudentView.put)
