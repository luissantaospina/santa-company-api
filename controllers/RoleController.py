from flask_restful import Resource
from models.Product import Role, RoleSchema
from flask_jwt_extended import jwt_required
from database.db import db
from flask import request

role_schema = RoleSchema()


class RolesController(Resource):

    @jwt_required()
    def get(self):
        roles = Role.query.all()
        return [role_schema.dump(role) for role in roles], 200

    @jwt_required()
    def post(self):
        role = Role(
            name=request.json["name"]
        )
        db.session.add(role)
        db.session.commit()
        return role_schema.dump(role), 200


class RoleController(Resource):

    @jwt_required()
    def get(self, id_role):
        role = Role.query.get_or_404(id_role)
        return role_schema.dump(role), 200

    @jwt_required()
    def delete(self, id_role):
        role = Role.query.get_or_404(id_role)
        db.session.delete(role)
        db.session.commit()
        return {'message': 'role deleted successfully'}, 200

    @jwt_required()
    def put(self, id_role):
        role = Role.query.get_or_404(id_role)
        role.name = request.json.get("name", role.name)
        db.session.commit()
        return role_schema.dump(role), 200
