from flask_restful import Resource
from models.models import Order, OrderSchema
from flask_jwt_extended import jwt_required
from database.db import db
from flask import request

order_schema = OrderSchema()


class OrdersController(Resource):

    @jwt_required()
    def get(self):
        orders = Order.query.all()
        return [order_schema.dump(order) for order in orders], 200

    @jwt_required()
    def post(self):
        order = Order(
            client_id=request.json["client_id"],
            code=request.json["code"],
            date_purchase=request.json["date_purchase"],
            price=request.json["price"]
        )
        db.session.add(order)
        db.session.commit()
        return order_schema.dump(order), 200


class OrderController(Resource):

    @jwt_required()
    def get(self, id_order):
        order = Order.query.get_or_404(id_order)
        return order_schema.dump(order), 200

    @jwt_required()
    def delete(self, id_order):
        order = Order.query.get_or_404(id_order)
        db.session.delete(order)
        db.session.commit()
        return {'message': 'order deleted successfully'}, 200

    @jwt_required()
    def put(self, id_order):
        order = Order.query.get_or_404(id_order)
        order.client_id = request.json.get("client_id", order.client_id)
        order.code = request.json.get("code", order.code)
        order.date_purchase = request.json.get("date_purchase", order.date_purchase)
        order.price = request.json.get("price", order.price)
        db.session.commit()
        return order_schema.dump(order), 200
