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
def display_c(text):
    '''display the character "C" followed
    by space and argument'''
    spaced_text = text.replace('_', ' ')
    return f"C {spaced_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    '''display the character "python" followed
    by space and argument'''
    spaced_text = text.replace('_', ' ')
    return f"Python {spaced_text}"


@app.route("/number/<n>", strict_slashes=False)
def display_number(n):
    '''display the number n if it's an integer'''
    coneverted_num = int(n)
    return f'{coneverted_num} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
