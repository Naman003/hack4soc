from flask import Blueprint, jsonify, request
from pymongo import MongoClient
client = MongoClient('mongodb+srv://cluster0.7bagwfz.mongodb.net',username='admin-naman', password='admin')

db = client.Users
api = Blueprint("api",__name__)
@api.route("/users", methods=["POST"])

def user():
    req = request.json
    if(not db.User.find_one({"uid":req['uid']})):
        db.User.insert_one({"uid":req['uid'], "name": req['name'], "email": req['email'], "isAdmin": False, "level": 1, "history": [], "curBookID": ""})
    dict = {}
    entry = db.User.find_one({"uid":req['uid']})
    for i in entry:
        if(i!="_id"):
            dict[i] = entry[i]
    print(dict)
    return jsonify(dict)
    
