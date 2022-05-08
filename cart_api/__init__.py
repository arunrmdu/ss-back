from flask_restful import Api
from app import app
from .cartApi import getUserCart,insertUserCart,deleteUserCart,updateCartQty

restServerInstance = Api(app)



restServerInstance.add_resource(getUserCart,"/api/v1.0/userCart/<string:u_id>")
restServerInstance.add_resource(insertUserCart,"/api/v1.0/insertUserCart/")
restServerInstance.add_resource(deleteUserCart,"/api/v1.0/deleteCart/<string:c_id>")

restServerInstance.add_resource(updateCartQty,'/api/v1.0/updateCart/')