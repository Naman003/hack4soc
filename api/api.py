from flask import Blueprint, jsonify
api = Blueprint("api",__name__)
@api.route("/user")
def user():
    return jsonify({"name":"Ready", "secret":7})
