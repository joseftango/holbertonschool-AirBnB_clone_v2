#!/usr/bin/python3
'''0-hello_route Module'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greed():
    '''displays "Hello HBNB!"'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''displays "HBNB"'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    '''display the character "C" followed
    by space and argument'''
    spaced_text = text.replace('_', ' ')
    return f"C {spaced_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
