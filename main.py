from flask import Flask, request
from services import max 

app = Flask(__name__)

@app.route("/access/")
def access():
    email = request.args.get('email')
    password = request.args.get('password')
    status = max.access(email, password)
    return status 

@app.route("/")
def main():
    return { 'status': 'Online' }