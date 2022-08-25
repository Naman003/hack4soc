from flask import Blueprint, jsonify
api = Blueprint("api",__name__)
@api.route("/users")
def user():
    return "Hello"
