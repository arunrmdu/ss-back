from calendar import c
from datetime import datetime, timedelta
from distutils.command.config import config
from turtle import back
from flask_restful import Resource
import logging as logger
from pymongo import MongoClient 
from config import config
from bson import ObjectId


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
        # output = []
        # output = [{item: str(x[item]) for item in x } for x in documents]
        output = [{item: str(x[item]) if item !='var' else x[item] for item in x } for x in documents]
        # for doc in documents:
        #     schema={}
        #     for item in doc:
        #         if item != 'var':
        #             schema[item]=str(doc[item])
        #         else:
        #             schema[item]=doc[item]

        #     output.append(schema)
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


class getProductById(Resource):
    def get(self,p_id):
        data={"filter":{"active":"Y","_id":ObjectId(str(p_id))}}
        data['database']="portal"
        data['collection']="inventory"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200
def removeduplicate(it):
    seen = []
    for x in it:
        t = tuple(x.items())
        if t not in seen:
            yield x
            seen.append(t)

class searchProduct(Resource):
    def get(self,term):
        data={"filter":{'$text': { '$search': str(term)}}}
        data['database']="portal"
        data['collection']="inventory"
        output= MongoAPI(data).read()
        data={"filter":{"active":"Y","cat":{"$regex": str(term), "$options": "i"}},"field":{"_id":1},"database":"portal","collection":"category"}
        
        response,c_ids=[],[]
        for x in  MongoAPI(data).read():
            c_ids.append(str(x['_id']))
        data={"filter":{"active":"Y","cat_id":{'$in':c_ids}},"database":"portal","collection":"inventory"}
        for items in MongoAPI(data).read():
            output.append(items)
        response=[item for item in removeduplicate(output)]
        return response,200
# {"name": {"$regex": "string", "$options": "i"}}