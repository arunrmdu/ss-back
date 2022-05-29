from calendar import c
from datetime import datetime, timedelta
from distutils.command.config import config
from turtle import back
from flask_restful import Resource,request
import logging as logger
from pymongo import MongoClient 
from config import config
from bson import json_util, ObjectId
import json
from flask_expects_json import expects_json
from .userschema import update_address_schema

class MongoAPI:
    def __init__(self, data):
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient(config['database']['mongo'])   
        database =data["database"] if "database" in data else "portal"
        collection = data["collection"] if "collection" in data else "users"
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
    def find_one(self):
        filter=self.data['filter'] if "filter" in self.data else {}
        field=self.data['field'] if "field" in self.data else {}
        output = self.collection.find_one(filter,field)
        output ['_id']= str(output["_id"])
        return output    
    def update(self):
        filt = self.data['filter']
        self.data['DataToBeUpdated']["update_dt"]=datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
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
            response=obj1.find_one()
            if response == []:
                return {"message":" Username and password combination not found. If you are new user please sign up"},200
            data={"filter":{"u_id":str(response['_id'])},"collection":"cart"}
            obj1 = MongoAPI(data)
            cart_response=obj1.read()
            response['cart']=cart_response
            return response,200

class verifyUser(Resource):
    def get(self,username):
        data={"filter":{"username":username},"field":{"username":1,"_id":0}}
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200
                 
class userAddress(Resource):
    def get(self,uid):
        uid=ObjectId(uid)
        data={"filter":{"_id":uid},"field":{"address_alt":1,"_id":0}}
        obj1 = MongoAPI(data)
        response=obj1.read()
        
        return json.loads(response[0]["address_alt"].strip("'<>() ").replace('\'', '\"')),200

class updateAddress(Resource):
    @expects_json(update_address_schema, ignore_for=['GET'])
    def post(self):
        post_data = request.get_json()
        data={'filter':{"_id":ObjectId(str(post_data["id"]))}}
        data["DataToBeUpdated"]={"address_alt":post_data["address"]}
        MongoAPI(data).update()
        data={'filter':{"_id":ObjectId(str(post_data["id"]))}}
        response=MongoAPI(data).read()
        return response,200