#!flask/bin/python
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


from views import *

# RUNTIME
if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True, threaded=True)
