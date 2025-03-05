#!/usr/bin/python3
'''0-hello_route Module'''
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    '''display the number n only if it's an integer'''
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_in_template(n):
    '''display the number n only if it's an integer'''
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
