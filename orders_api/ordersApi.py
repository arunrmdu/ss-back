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
from .schema import orders_schema,delete_schema,update_schema,insert_schema




class MongoAPI:
    def __init__(self, data):
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient(config['database']['mongo'])   
        database =data["database"] if "database" in data else "portal"
        collection = data["collection"] if "collection" in data else "orders"
        cursor = self.client[database]
        self.collection = cursor[collection]
        # db = self.client.portal
        # self.mycol = db.category
        self.data=data
    def read(self):
        filter=self.data['filter'] if "filter" in self.data else {}
        field=self.data['field'] if "field" in self.data else {}
        documents = self.collection.find(filter,field)
        output = [{item: str(x[item]) if item !='items' and item!='var' else x[item] for item in x } for x in documents]
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
        self.data['DataToBeUpdated']["update_dt"]=datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self):
        filt = self.data['filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
    def delete_all(self):
        filt = self.data['filter']
        response = self.collection.delete_many(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
    
    def increment(self):
        filt = self.data['filter']
        update_data={"$inc":self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, update_data)
        return response


class getUserOrders(Resource):
    def get(self,u_id):
        data={"filter":{"u_id":str(u_id)}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

class placeOrder(Resource):
    @expects_json(orders_schema, ignore_for=['GET'])
    def post(self):
        post_data = request.get_json()
        data={"collection":"cart","filter":{"u_id":str(post_data['u_id']),"active":"Y"}}
        cart_response=MongoAPI(data).read()
        MongoAPI(data).delete_all()
        post_data['ins_dt']=str(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"))
        post_data['update_dt']=str(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"))
        schema=insert_schema()
        ins_data=json.loads(schema.dumps(post_data))
        ins_data['items']=cart_response
        data={"collection":"orders","Document":ins_data}
        MongoAPI(data).write(data)
        
            
        data={"filter":{"u_id":str(post_data['u_id'])}}
        obj=MongoAPI(data)
        response=obj.read()
        return response,200

