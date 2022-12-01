from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

#creating a student table for inserting data into database

class student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    age = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(200))
