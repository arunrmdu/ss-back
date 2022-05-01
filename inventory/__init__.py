from flask_restful import Api
from app import app
from .inventoryAPI import getAllProduct,getSubCategoryById


restServerInstance = Api(app)

restServerInstance.add_resource(getAllProduct,"/api/v1.0/allProducts/")
# restServerInstance.add_resource(getSubCategoryById,"/api/v1.0/subCategory/<string:cat_id>")