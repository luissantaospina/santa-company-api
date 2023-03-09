from flask_restful import Resource
from flask import request


class OrderController(Resource):

    def get(self):
        return '', 200
