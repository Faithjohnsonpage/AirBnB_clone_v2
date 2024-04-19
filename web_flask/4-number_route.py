#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    # display “Hello HBNB!”
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # display “HBNB”
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    # display “C” followed by the value of the text variable
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text=''):
    # display “Python” followed by the value of the text variable
    if '_' in text:
        text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # display “n is a number” only if n is an integer
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
