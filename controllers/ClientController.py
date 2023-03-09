from flask_restful import Resource
from models.models import Client, ClientSchema
from flask_jwt_extended import jwt_required
from database.db import db
from flask import request

client_schema = ClientSchema()


class ClientsController(Resource):

    @jwt_required()
    def get(self):
        clients = Client.query.all()
        return [client_schema.dump(client) for client in clients], 200

    @jwt_required()
    def post(self):
        client = Client(
            email=request.json["email"],
            name=request.json["name"],
            password=request.json["password"]
        )
        db.session.add(client)
        db.session.commit()
        return client_schema.dump(client), 200


class ClientController(Resource):

    @jwt_required()
    def get(self, id_client):
        client = Client.query.get_or_404(id_client)
        return client_schema.dump(client), 200

    @jwt_required()
    def delete(self, id_client):
        client = Client.query.get_or_404(id_client)
        db.session.delete(client)
        db.session.commit()
        return {'message': 'client deleted successfully'}, 200

    @jwt_required()
    def put(self, id_client):
        client = Client.query.get_or_404(id_client)
        client.email = request.json.get("email", client.email)
        client.name = request.json.get("name", client.name)
        client.password = request.json.get("password", client.password)
        db.session.commit()
        return client_schema.dump(client), 200
