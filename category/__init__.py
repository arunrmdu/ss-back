from flask_restful import Api
from app import app
from .categoryAPI import getCategory,getSubCategoryById,getAllCategory


restServerInstance = Api(app)

restServerInstance.add_resource(getCategory,"/api/v1.0/category/<string:supplier>")
restServerInstance.add_resource(getSubCategoryById,"/api/v1.0/subCategory/<string:cat_id>")
restServerInstance.add_resource(getAllCategory,"/api/v1.0/allCategory/")