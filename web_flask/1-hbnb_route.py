#!/usr/bin/python3
'''0-hello_route Module'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greed():
    '''displays "Hello HBNB!"'''
    return "Hello HBNB!"


@app.route("/HBNB", strict_slashes=False)
def HBNB():
    '''displays "HBNB"'''
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
