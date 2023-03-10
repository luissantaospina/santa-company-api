from flask import Flask
from config import DevelopmentConfig
from flask_restful import Api
from controllers.ProductController import ProductsController, ProductController
from controllers.RoleController import RolesController, RoleController
from controllers.ClientController import ClientsController, ClientController
from controllers.OrderController import OrdersController, OrderController
from controllers.UserController import UsersController, UserController
from controllers.AuthController import AuthController
from helpers.Errors import Errors
from models.models import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app_context = app.app_context()
app_context.push()
app.config.from_object(DevelopmentConfig)

db.init_app(app)
db.create_all()

api = Api(app)

api.add_resource(AuthController, '/api/v1/auth/login')

api.add_resource(ProductsController, '/api/v1/auth/products')
api.add_resource(ProductController, '/api/v1/auth/product/<int:id_product>')

api.add_resource(RolesController, '/api/v1/auth/roles')
api.add_resource(RoleController, '/api/v1/auth/role/<int:id_role>')

api.add_resource(ClientsController, '/api/v1/auth/clients')
api.add_resource(ClientController, '/api/v1/auth/client/<int:id_client>')

api.add_resource(UsersController, '/api/v1/auth/users')
api.add_resource(UserController, '/api/v1/auth/user/<int:id_user>')

api.add_resource(OrdersController, '/api/v1/auth/orders')
api.add_resource(OrderController, '/api/v1/auth/order/<int:id_order>')


jwt = JWTManager(app)

if __name__ == '__main__':
    app.register_error_handler(404, Errors.page_not_found)
    app.register_error_handler(405, Errors.method_not_allowed)
    app.register_error_handler(500, Errors.server_error)

    app.run(debug=True)
