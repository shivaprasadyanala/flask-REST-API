from flask import request, render_template, redirect, url_for, Flask, jsonify
from models.student import student, db
from services.student_service import create_logic
from schemas.schema import StudentSchema

student_schema = StudentSchema()


def index():
    try:
        users = student.query.all()
        student_schema = StudentSchema(many=True)
        data = student_schema.dump(users)
        response = jsonify(
            {"message": "data fetched succesfully", "data": data})
        response.status_code = 200
    except Exception as error:
        response = jsonify({"message": "errror", "error": str(error)})
        response.status_code = 400
    return response


def create():
    create_logic()


# insert data into table.
def insert():
    try:
        if request.method == 'POST':
            s = student(
                name=request.form['name'],
                age=request.form['age'],
                location=request.form['location']
            )
            db.session.add(s)
            db.session.commit()
            data = student_schema.dump(s)
            response = jsonify(
                {"message": "data inserted succusfully", "data": data})
    except Exception as error:
        response = jsonify(
            {"message": "error in inserting data", "error": str(error)})
        response.status_code = 400
    return response


def delete(id):
    try:
        user = db.get_or_404(student, id)
        db.session.delete(user)
        db.session.commit()
        data = student_schema.dump(user)
        response = jsonify(
            {"message": "data deleted succusfully", "data": data})
    except Exception as error:
        response = jsonify(
            {"message": "error in deleting data", "error": str(error)})
        response.status_code = 400
    return response


def update(id):
    try:
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
            response = jsonify(
                {"message": "data updated succusfully", "data": data})
    except Exception as error:
        response = jsonify(
            {"message": "error in updating data", "error": str(error)})
        response.status_code = 400
    return response
