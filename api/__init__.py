from flask_restful import Api
from app import app
from .TaskAPI import Task
from .TaskByIDAPI import TaskByID


restServerInstance = Api(app)

restServerInstance.add_resource(Task,"/api/v1.0/task")
restServerInstance.add_resource(TaskByID,"/api/v1.0/task/id/<string:taskId>")
