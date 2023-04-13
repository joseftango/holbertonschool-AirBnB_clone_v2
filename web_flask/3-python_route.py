#!/usr/bin/python3
"""module named 3-python_route"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_1():
    """function that display Hello HBNB! in page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_2():
    """function that display HBNB in page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_3(text):
    """function that display text in page"""
    str = "C" + " " + text.replace("_", " ")
    return str


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_4(text):
    """function that display text in page"""
    str = "Python " + text.replace("_", " ")
    return str


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
