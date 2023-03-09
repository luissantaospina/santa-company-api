from flask_restful import Resource
from models.Product import User
from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


class AuthController(Resource):

    @classmethod
    def post(cls):
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        user = User.query.filter_by(email=email).first()
        if user is None or not check_password_hash(user.password, password):
            return {'mensaje': 'Credentials invalid'}, 401

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200
