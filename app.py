from flask import Flask, make_response, jsonify
from api.api import api
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.register_blueprint(api, url_prefix='/api')
# @app.route('/api/user')
# def hello():
#     return jsonify({"name":"Ready", "secret":7})

