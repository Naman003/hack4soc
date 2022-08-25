from flask import Flask, make_response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/api/user')
def hello():
    return jsonify({"name":"Ready", "secret":7})

