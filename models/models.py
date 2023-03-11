from database.db import db
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime

db = db

permission_roles = db.Table(
    'permission_roles',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True, nullable=False),
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
    db.Column('created_at', db.DateTime, default=datetime.utcnow),
    db.Column('updated_at', db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
)


class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    roles = db.relationship('Role', secondary='permission_roles', back_populates='permissions')


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    users = db.relationship('User', backref='role', lazy=True, viewonly=True)
    permissions = db.relationship('Permission', secondary=permission_roles, back_populates='roles')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    orders = db.relationship('Order', backref='client', lazy=True, viewonly=True)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    date_purchase = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


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
    updated_at = fields.DateTime()


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
    updated_at = fields.DateTime()


class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    name = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    code = fields.String()
    date_purchase = fields.DateTime()
    price = fields.Float()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ClientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class PermissionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Permission
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.Integer()
    name = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
