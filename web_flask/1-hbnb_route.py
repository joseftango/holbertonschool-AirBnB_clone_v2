#!/usr/bin/python3
'''0-hello_route Module'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def first_greed():
    '''displays the returned text'''
    return "Hello HBNB!"


@app.route("/HBNB", strict_slashes=False)
def second_greed():
    '''displays the returned text'''
    return "Hello HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
