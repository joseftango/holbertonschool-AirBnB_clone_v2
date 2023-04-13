#!/usr/bin/python3
"""module named 0-hello_route"""
from flask import Flask


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def display_1():
    """function that display text in page"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
