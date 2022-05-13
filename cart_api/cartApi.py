from datetime import datetime, timedelta
from re import M
import re,json
from turtle import back
from flask_restful import Resource,request
import logging as logger
from pymongo import MongoClient 
from bson import json_util, ObjectId
from config import config
from flask_expects_json import expects_json
from .schema import cart_schema,delete_schema,update_schema



class MongoAPI:
    def __init__(self, data):
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient(config['database']['mongo'])   
        database =data["database"] if "database" in data else "portal"
        collection = data["collection"] if "collection" in data else "cart"
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
    def write(self, data):
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        id=str(response.inserted_id)
        output = {'Status': 'Added to Cart',
                  'Document_ID': id}
        return json.loads(json_util.dumps(output))
    def update(self):
        filt = self.data['filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self):
        filt = self.data['filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
    
    def increment(self):
        filt = self.data['filter']
        update_data={"$inc":self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, update_data)
        return response


class getUserCart(Resource):
    def get(self,u_id):
        data={"filter":{"u_id":str(u_id),"active":"Y"}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

class insertUserCart(Resource):
    @expects_json(cart_schema, ignore_for=['GET'])
    def post(self):
        post_data = request.get_json()
        post_data['qty'] ="1"
        post_data['active'] ="Y"
        data={'Document':post_data}
        MongoAPI(data).write(data)
        data={"filter":{"u_id":str(post_data['u_id'])}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

class deleteUserCart(Resource):
    @expects_json(cart_schema, ignore_for=['GET'])
    def post(self):
        post_data = request.get_json()
        data={'filter':{"_id":ObjectId(str(post_data["_id"]))}}
        MongoAPI(data).delete()
        data={"filter":{"u_id":str(post_data["u_id"])}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

class updateCartQty(Resource):
    @expects_json(update_schema, ignore_for=['GET'])
    def post(self):
        post_data = request.get_json()
        data={'filter':{"_id":ObjectId(str(post_data["c_id"]))}}
        if "+" in str(post_data['qty']):
            data["DataToBeUpdated"]={"qty":1}
            MongoAPI(data).increment()
        else:
            response=MongoAPI(data).find_one()
            if int(response['qty']) <= 1:
                MongoAPI(data).delete() 
            else:
                data["DataToBeUpdated"]={"qty":-1}
                MongoAPI(data).increment()
        data={'filter':{"_id":ObjectId(str(post_data["c_id"]))}}
        response=MongoAPI(data).read()    
        return response,200

class addtoWishList(Resource):
    def get(self,c_id):
        cart_id=ObjectId(c_id)
        data={'filter':{"_id":cart_id},"DataToBeUpdated":{"active":"N"}}
        response=MongoAPI(data).find_one()

        MongoAPI(data).update()
        u_id=response['u_id']
        data={"filter":{"u_id":str(u_id),"active":"Y"}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

class getwishList(Resource):
    def get(self,u_id):
        data={"filter":{"u_id":str(u_id),"active":"N"}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200


class wishListtoCart(Resource):
    def get(self,c_id):
        cart_id=ObjectId(c_id)
        data={'filter':{"_id":cart_id},"DataToBeUpdated":{"active":"Y"}}
        response=MongoAPI(data).find_one()

        MongoAPI(data).update()
        u_id=response['u_id']
        data={"filter":{"u_id":str(u_id),"active":"Y"}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

