from flask_restful import Api
from app import app
from .HealthAPI import HealthCheck


restServerInstance = Api(app)

restServerInstance.add_resource(HealthCheck,"/api/v1.0/healthCheck")
# restServerInstance.add_resource(HealthCheck,"/")
