from flask_restful import Api
from app import app
from .HealthAPI import HealthCheck


restServerInstance = Api(app)

restServerInstance.add_resource(HealthCheck,"/healthCheck")
# restServerInstance.add_resource(HealthCheck,"/")

# restServerInstance.init_app(app)