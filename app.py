from flask import Flask, make_response, request, jsonify
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

JWTSECRET = "secret123" # Get from env

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    token = jwt.encode({
        'userid': 101,
        'exp': datetime.utcnow() + timedelta(minutes=5)
    }, JWTSECRET)

    return make_response(jsonify({'token': token}), 201)

@app.route("/protected")
def proto():
    
    return jsonify({'protected': 'protected'})

@app.route("/")
def unproto():
    
    return jsonify({'open': 'open'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')