from flask_restful import Api
from app import app
from .cattApi import getUserCart,insertUserCart

restServerInstance = Api(app)



restServerInstance.add_resource(getUserCart,"/api/v1.0/userCart/<string:u_id>")
restServerInstance.add_resource(insertUserCart,"/api/v1.0/insertUserCart/")