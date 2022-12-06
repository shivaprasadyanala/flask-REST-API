import jwt
from flask import request, jsonify
from models.student import register, db
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message": "Token is missing"})
        try:
            print("hi")
            data = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(data)
            current_user = register.query.filter_by(id=data['id']).first()
        except Exception as error:
            return jsonify(
                {"message": "invalid token", "error": str(error)})
            response.status_code = 400
        return f(current_user, *args, **kwargs)
    return decorated
