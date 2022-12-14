import os
from flask import Flask, request, g
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
# from config import app_config
# from routes.register import reg_blueprint
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config['MAIL_SERVER'] = os.environ['EMAIL_HOST']
app.config['MAIL_PORT'] = os.environ['EMAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['EMAIL_HOST_USER']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_HOST_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
db = SQLAlchemy(app)


def get_app():
    db.init_app(app)

    migrate = Migrate(app, db)
    from models import student
    from routes import product, register
    app.register_blueprint(register.reg_blueprint)
    return app
