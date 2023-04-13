#!/usr/bin/python3
"""model named 6-number_odd_or_even"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def display_an_integer(n):
    """fucntion that displays n is a number if n is integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_template(n):
    """fucntion that displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_template2(n):
    """display a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
