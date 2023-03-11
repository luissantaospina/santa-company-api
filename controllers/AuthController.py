from flask_restful import Resource
from models.models import User, UserSchema, Permission, PermissionSchema
from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

user_schema = UserSchema()
permission_schema = PermissionSchema()


class AuthController(Resource):

    @classmethod
    def post(cls):
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        # password = 'luis'
        # password_hash = generate_password_hash(password, method='sha256')
        # print(password_hash)

        user = User.query.filter_by(email=email).first()

        if user is None or not check_password_hash(user.password, password):
            return {'mensaje': 'Credentials invalid'}, 401

        access_token = create_access_token(identity=user.id)
        permissions_by_role = user.role.permissions
        permissions_user = []

        for permission_by_role in permissions_by_role:
            permissions_user.append(permission_by_role.name)

        return {
            'access_token': access_token,
            'user': user_schema.dump(user),
            'permissions': permissions_user
        }, 200
