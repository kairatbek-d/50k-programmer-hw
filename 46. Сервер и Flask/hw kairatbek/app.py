from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def homepage():
    return Response("Welcome to the site!")

@app.route('/test/')
def test():
    return Response("Test")