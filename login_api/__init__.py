from flask_restful import Api
from app import app
from .loginApi import authticateUser
from .registerUserApi import registerUser,verifyUser
from .userApi import getusers
from flask_cors import CORS , cross_origin


restServerInstance = Api(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

restServerInstance.add_resource(authticateUser,"/api/v1.0/auth")
restServerInstance.add_resource(registerUser,"/api/v1.0/registerUser")
restServerInstance.add_resource(verifyUser,"/api/v1.0/verifyUser")
restServerInstance.add_resource(getusers,"/api/v1.0/getusers")