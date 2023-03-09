from database.db import db
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime

db = db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer)
    category = db.Column(db.String(100))
    code = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    amount = fields.Integer()
    category = fields.String()
    code = fields.String()
    description = fields.String()
    is_active = fields.Boolean()
    name = fields.String()
    price = fields.Float()
    created_at = fields.DateTime()
    update_at = fields.DateTime()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    update_at = fields.DateTime()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    name = fields.String()
    created_at = fields.DateTime()
    update_at = fields.DateTime()
