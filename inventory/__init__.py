from flask_restful import Api
from app import app
from .inventoryAPI import getAllNewProduct, getAllPopularProduct, getAllProduct, getProductByCatID,getProductByParentCatID,getProductById,searchProduct


restServerInstance = Api(app)

restServerInstance.add_resource(getAllProduct,"/api/v1.0/allProducts/")
restServerInstance.add_resource(getAllPopularProduct,"/api/v1.0/allPopularProduct/")
restServerInstance.add_resource(getAllNewProduct,"/api/v1.0/allNewProduct/")
restServerInstance.add_resource(getProductByCatID,"/api/v1.0/productByCategoryID/<string:cat_id>")
restServerInstance.add_resource(getProductByParentCatID,"/api/v1.0/productByp_CategoryID/<string:cat_id>")
restServerInstance.add_resource(getProductById,"/api/v1.0/productByID/<string:p_id>")
restServerInstance.add_resource(searchProduct,"/api/v1.0/search/<string:term>")
# restServerInstance.add_resource(getAllProduct,"/api/v1.0/allProducts/")
# restServerInstance.add_resource(getAllProduct,"/api/v1.0/allProducts/")
# restServerInstance.add_resource(getSubCategoryById,"/api/v1.0/subCategory/<string:cat_id>")