from flask_restful import Resource
from models.Product import Product, ProductSchema
from flask_jwt_extended import jwt_required
from database.db import db
from flask import request

product_schema = ProductSchema()


class ProductsController(Resource):

    @jwt_required()
    def get(self):
        products = Product.query.all()
        return [product_schema.dump(product) for product in products], 200

    @jwt_required()
    def post(self):
        product = Product(
            amount=request.json["amount"],
            category=request.json["category"],
            code=request.json["code"],
            description=request.json["description"],
            name=request.json["name"],
            price=request.json["price"]
        )
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product), 200


class ProductController(Resource):

    @jwt_required()
    def get(self, id_product):
        product = Product.query.get_or_404(id_product)
        return product_schema.dump(product), 200

    @jwt_required()
    def delete(self, id_product):
        product = Product.query.get_or_404(id_product)
        db.session.delete(product)
        db.session.commit()
        return {'message': 'product deleted successfully'}, 200

    @jwt_required()
    def put(self, id_product):
        product = Product.query.get_or_404(id_product)
        product.amount = request.json.get("amount", product.amount)
        product.category = request.json.get("category", product.category)
        product.code = request.json.get("code", product.code)
        product.description = request.json.get("description", product.description)
        product.name = request.json.get("name", product.name)
        product.price = request.json.get("price", product.price)
        db.session.commit()
        return product_schema.dump(product), 200
