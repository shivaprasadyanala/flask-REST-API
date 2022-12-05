from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# creating a student table for inserting data into database


class student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200))

# creating a register table for inserting data into database


class register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
