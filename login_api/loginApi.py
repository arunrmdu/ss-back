from flask_restful import Resource,request
import logging as logger
import json,base64
import pandas as pd

class authticateUser(Resource):
    def __init__(self):
        self.data = pd.read_csv("./data/user.csv")
    def post(self):
        logger.debug("Inside the authentication post method")
        post_data = request.get_json()  
        if "username" not in post_data or "password" not in post_data:
            return {"message":" username and password needed"},200
        else:
            data_found=json.loads(self.data.loc[self.data['username'] == post_data['username']].to_json(orient="records"))
            if data_found != []:
                if str(data_found[0]["password"]) == str(post_data["password"]):
                    token=str(base64.b64encode(post_data["username"].encode()).decode())
                    return{"message":"authenticated successfully","username":str(post_data["username"]),"token":str(token)},200
                else:
                    return{"message":"username or password is not correct, Please try again"},200
            else:
                return{"message":"username is not found, Please register if new user"},200
        return {"message" : "Inside post method"},200


    def get(self):
        logger.debug("Inisde the get method of Task")
        return {"message" : "Inside get method"},200






