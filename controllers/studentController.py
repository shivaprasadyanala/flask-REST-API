from flask import request, render_template, redirect, url_for, Flask, jsonify
from models.student import student, db
from services.student_service import create_logic
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "age", "location", "_links")

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("blueprint.index"),
            "collection": ma.URLFor("blueprint.index")}
    )


student_schema = StudentSchema()


def index():
    users = student.query.all()
    student_schema = StudentSchema(many=True)
    return student_schema.jsonify(users)


def create():
    create_logic()


# insert data into table.
def insert():
    if request.method == 'POST':
        s = student(
            name=request.form['name'],
            age=request.form['age'],
            location=request.form['location']
        )
        db.session.add(s)
        db.session.commit()
        response = student_schema.dump(s)
        return jsonify({"message": "data inserted succusfully", "data": response})


def delete(id):
    user = db.get_or_404(student, id)
    # user = student.query.filter_by(id=id).first()
    # if request.method == "POST":
    db.session.delete(user)
    db.session.commit()
    data = student_schema.dump(user)
    return jsonify({"message": "data deleted succusfully", "data": data})


def update(id):
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        stu = student.query.filter_by(id=id).first()

        name = request.form['name'],
        age = request.form['age'],
        location = request.form['location']
        stu.name = name
        stu.age = age
        stu.location = location
        db.session.add(stu)
        db.session.commit()
        data = student_schema.dump(stu)
        return jsonify({"message": "data updated succusfully", "data": data})
