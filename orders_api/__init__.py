from flask_restful import Api
from app import app
from .ordersApi import getUserOrders,placeOrder

restServerInstance = Api(app)



restServerInstance.add_resource(getUserOrders,"/api/v1.0/userOrders/<string:u_id>")
restServerInstance.add_resource(placeOrder,"/api/v1.0/placeOrder")
