#!/bin/usr/python3
"""module named 1-hbnb_route"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_1():
    """function that display text in page"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_2():
	"""function that display text in page"""
	return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
