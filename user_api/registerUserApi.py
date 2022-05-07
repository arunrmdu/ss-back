from flask_restful import Resource,request
import logging as logger
import json,base64
import pandas as pd

class registerUser(Resource):
    def __init__(self):
        
        self.data = pd.read_csv("./data/user.csv")
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
        logger.debug("Inisde the get method of Task")
        return {"message" : "Inside get method"},200


class verifyUser(Resource):
    def __init__(self):
        
        self.data = pd.read_csv("./data/user.csv")
    def post(self):
        post_data = request.get_json()  
        if "username" not in post_data:
             return {"message":" username is needed"},200
        else:
            if((self.data['username']==post_data["username"]).any()):
                return {"message": 'Username already taken please create new.'}
            else:
                return{"message":"Username available ","username":str(post_data["username"])},200
        # return {"message" : "Inside post method"},200





