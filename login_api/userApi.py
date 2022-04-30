from flask_restful import Resource,request
from flask import jsonify
import logging as logger
import json,base64
import pandas as pd





class getusers(Resource):
    def __init__(self):
        
        self.data = pd.read_csv("./data/user.csv" ,usecols = ['username','email','phone_no','status'], low_memory = True)
    def post(self):
        post_data = request.get_json()  
        if "username" not in post_data or "password" not in post_data or "email" not in post_data or "phone_no" not in post_data:
             return {"message":" username and password needed"},200
        else:
            if((self.data['username']==post_data["username"]).any()):
                return {"message": 'ID already taken please create new id or ID yet to be activated pleaes check back later'},200
            else:
                post_data["status"] = "inacitive"
                self.data= self.data.append(post_data, ignore_index=True)
                self.data.to_csv("./data/user.csv", index=False)
                return{"message":"registered successfully","username":str(post_data["username"])},200
        # return {"message" : "Inside post method"},200


    def get(self):
        
        return json.loads(self.data.to_json(orient="records")),200
