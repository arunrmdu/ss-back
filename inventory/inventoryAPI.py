from calendar import c
from datetime import datetime, timedelta
from distutils.command.config import config
from turtle import back
from flask_restful import Resource
import logging as logger
from pymongo import MongoClient 
from config import config

class MongoAPI:
    def __init__(self, data):
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient(config['database']['mongo'])   
        database = data['database']
        collection = data['collection']
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


class getAllProduct(Resource):
    def get(self):
        data={"filter":{"active":"Y"}}
        data['database']="portal"
        data['collection']="inventory"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200


class getAllPopularProduct(Resource):
    def get(self):
        data={"filter":{"active":"Y","is_popular":"Y"}}
        data['database']="portal"
        data['collection']="inventory"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200

class getAllNewProduct(Resource):
    def get(self):
        to_date=datetime.now()-timedelta(int(config['generic']['to_date_for_new_product']))
        data={"filter":{"active":"Y",'ins_dt': {'$gt': to_date}}}
        data['database']="portal"
        data['collection']="inventory"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200

class getProductByCatID(Resource):
    def get(self,cat_id):
        data={"filter":{"active":"Y","cat_id":cat_id}}
        data['database']="portal"
        data['collection']="inventory"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200

class getProductByParentCatID(Resource):
    def get(self,cat_id):
        data={"filter":{"active":"Y","p_cat":cat_id},"field":{"_id":1},"database":"portal","collection":"category"}
        obj1 = MongoAPI(data)
        c_ids=[]
        for x in obj1.read():
            c_ids.append(str(x['_id']))
        if c_ids ==[]:
            data={"filter":{"active":"Y","cat_id":cat_id},"database":"portal","collection":"inventory"}
        else:
            data={"filter":{"active":"Y","cat_id":{'$in':c_ids}},"database":"portal","collection":"inventory"}
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200



