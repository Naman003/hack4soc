from flask import Flask, make_response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/api/user')
def hello():
    return jsonify({"name":"Ready", "secret":6})

if(__name__=='__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)