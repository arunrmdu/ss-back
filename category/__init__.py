from flask_restful import Api
from app import app
from .categoryAPI import getCategory,getSubCategoryById


restServerInstance = Api(app)

restServerInstance.add_resource(getCategory,"/api/v1.0/catgory/<string:supplier>")
restServerInstance.add_resource(getSubCategoryById,"/api/v1.0/subCatgory/<string:cat_id>")