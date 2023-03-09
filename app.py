from flask import Flask
from config import DevelopmentConfig
from flask_restful import Api
from controllers.OrderController import OrderController

app = Flask(__name__)
app_context = app.app_context()
app_context.push()
app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(OrderController, '/orders')

if __name__ == '__main__':

    app.run()
