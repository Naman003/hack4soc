from flask import Flask, make_response, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import bson
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
client = MongoClient('mongodb+srv://cluster0.7bagwfz.mongodb.net',username='admin-naman', password='admin')
from routes import api
db = client.Users
validator_book = {
    "$jsonSchema":{
        "bsonType": "object",
        "required": ['bookID', 'level', 'genre', 'title', 'author'],
        "properties": { 
            "bookID": {
                "bsonType": "string",
                "description": "Unique identifier for book"
            },
            "level": {
                "bsonType": "int",
                "description": "The current level of the book"
            },
            "genre": {
                "bsonType": "string",
                "description": "Genre of the book"
            },
            "title": {
                "bsonType": "string",
                "description": "Title of the book"
            },
            "author": {
                "bsonType": "string",
                "description": "Author of the book"
            },
            "picture": {
                "bsonType": "binData"
            }
        }
    }
}

validator_user = {
    "$jsonSchema":{
        "bsonType": "object",
        "required": ['uid','level', "name", "email", "isAdmin"],
        "properties": {
            "uid": {
                "bsonType": "string",
                "description": "Unique identifier for user"
            },
            "history": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": ['bookID', 'summary'],
                    "properties": {
                        "bookID": {
                            "bsonType": "string",
                            "description": "Book Id"
                        },
                        "summary": {
                            "bsonType": "string",
                            "description": "Summary"
                        }
                    },
                    "description": "Book history details"
                },
                "description": "Array of books"
            },
            "level": {
                "bsonType": "int",
                "description": "Current level of the user"
            },
            "curBookID": {
                "bsonType": "string",
                "description": "Id of current book"
            },
            "name": {
                "bsonType": "string",
                "description": "Name of user"
            },
            "email": {
                "bsonType": "string",
                "description": "Email of user"
            },
            "isAdmin": {
                "bsonType": "bool",
                "description": "Is the user a admin"
            },
        }
    }
}

def createCollection(collName):
    if(not (collName in db.list_collection_names())):
        db.create_collection(collName)

# createCollection("Book")
# createCollection("User")
db.command("collMod","Book",validator=validator_book)
db.command("collMod","User",validator=validator_user)
# print(db.User.find_one({"userID": 1}))
# try:
#     db.myT.insert_one({"username":"nmn","password":"nmn"})
# except Exception as e:
#     print(e)

app.register_blueprint(api, url_prefix='/api')

