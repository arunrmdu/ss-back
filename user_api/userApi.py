from calendar import c
from datetime import datetime, timedelta
from distutils.command.config import config
from turtle import back
from flask_restful import Resource,request
import logging as logger
from pymongo import MongoClient 
from config import config

class MongoAPI:
    def __init__(self, data):
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient(config['database']['mongo'])   
        database ="portal"
        collection = "users"
        cursor = self.client[database]
        self.collection = cursor[collection]
        # db = self.client.portal
        # self.mycol = db.category
        self.data=data
    def read(self):
        filter=self.data['filter'] if "filter" in self.data else {}
        field=self.data['field'] if "field" in self.data else {}
        documents = self.collection.find(filter,field)
        output = [{item: str(x[item]) for item in x } for x in documents]
        return output    


class authticateUser(Resource):
    def get(self):
        response={"message":"i am running fine!"}
        return response,200
    def post(self):
        post_data = request.get_json()
        print(post_data)
        if "username" not in post_data or "password" not in post_data:
            return {"message":" username and password needed"},200
        else:
            data={"filter":{"active":"Y","username":str(post_data['username']),"password":str(post_data['password'])}}
            obj1 = MongoAPI(data)
            response=obj1.read()
            if response == []:
                return {"message":" Username and password combination not found. If you are new user please sign up"},200
            return response,200

class verifyUser(Resource):
    def get(self,username):
        data={"filter":{"username":username},"field":{"username":1,"_id":0}}
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200
                 
