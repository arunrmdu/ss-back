from flask_restful import Api
from app import app
from .cartApi import getUserCart,insertUserCart,deleteUserCart,updateCartQty,addtoWishList,getwishList,wishListtoCart

restServerInstance = Api(app)



restServerInstance.add_resource(getUserCart,"/api/v1.0/userCart/<string:u_id>")
restServerInstance.add_resource(insertUserCart,"/api/v1.0/insertUserCart/")
restServerInstance.add_resource(deleteUserCart,"/api/v1.0/deleteCart/")

restServerInstance.add_resource(updateCartQty,'/api/v1.0/updateCart/')
restServerInstance.add_resource(addtoWishList,'/api/v1.0/addtoWishList/<string:c_id>')
restServerInstance.add_resource(getwishList,'/api/v1.0/getwishList/<string:u_id>')
restServerInstance.add_resource(wishListtoCart,'/api/v1.0/wishListtoCart/<string:u_id>')