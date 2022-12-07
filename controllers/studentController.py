from flask import request, render_template, redirect, url_for, Flask, jsonify, views
from models.student import student, db
from services.student_service import create_logic
from schemas.schema import StudentSchema

student_schema = StudentSchema()

app = Flask(__name__)

# test branch
# test2 branch


class StudentView(views.MethodView):

    def get():
        try:
            users = student.query.all()
            student_schema = StudentSchema(many=True)
            # serilazing users i.e, converting to json() format
            data = student_schema.dump(users)
            response = jsonify(
                {"message": "data fetched succesfully", "data": data})
            response.status_code = 200
        except Exception as error:
            response = jsonify({"message": "errror", "error": str(error)})
            response.status_code = 400
        return response

    # insert data into table.

    def post():
        try:
            if request.method == 'POST':
                # s = student(
                #     name=request.form['name'],
                #     age=request.form['age'],
                #     location=request.form['location']
                # )
                request_data = request.json
                print(request_data)
                student_object = StudentSchema.load(data=request_data)
                db.session.add(student_object)
                db.session.commit()
                # data = student_schema.dump(student_object)
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

    def put(id):
        try:
            if request.method == "PUT":
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


# app.add_url_rule('/',view_func=StudentView.as_view('index'))
