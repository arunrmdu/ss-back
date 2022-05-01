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
        output = [x for x in documents]
        return output    


class getCategory(Resource):
    def get(self,supplier):
        data={"filter":{"supp":str(supplier),"active":"Y","p_cat":"-"},"field":{"cat":1}}
        data['database']="portal"
        data['collection']="category"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200

class getSubCategoryById(Resource):
    def get(self,cat_id):
        data={"filter":{"active":"Y","p_cat":cat_id},"field":{"cat":1}}
        data['database']="portal"
        data['collection']="category"
        obj1 = MongoAPI(data)
        response=obj1.read()
        return response,200





