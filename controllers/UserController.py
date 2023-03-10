from flask_restful import Resource
from models.models import User, UserSchema
from flask_jwt_extended import jwt_required
from database.db import db
from flask import request
from werkzeug.security import generate_password_hash

user_schema = UserSchema()


class UsersController(Resource):

    @jwt_required()
    def get(self):
        users = User.query.all()
        return [user_schema.dump(user) for user in users], 200

    @jwt_required()
    def post(self):
        encrypted_password = generate_password_hash(request.json["password"], method='sha256')

        user = User(
            role_id=request.json["role_id"],
            email=request.json["email"],
            name=request.json["name"],
            password=encrypted_password
        )
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 200


class UserController(Resource):

    @jwt_required()
    def get(self, id_user):
        user = User.query.get_or_404(id_user)
        return user_schema.dump(user), 200

    @jwt_required()
    def delete(self, id_user):
        print(id_user)
        user = User.query.get_or_404(id_user)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'user deleted successfully'}, 200

    @jwt_required()
    def put(self, id_user):
        user = User.query.get_or_404(id_user)
        encrypted_password = generate_password_hash(request.json.get("password"), method='sha256')
        user.role_id = request.json.get("role_id", user.role_id)
        user.email = request.json.get("email", user.email)
        user.name = request.json.get("name", user.name)
        user.password = encrypted_password
        db.session.commit()
        return user_schema.dump(user), 200
