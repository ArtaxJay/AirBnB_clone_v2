#!/usr/bin/python3
"""
This is the app.py module for this flask project
# Import the flask class from its module
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Listen/link to the home url """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Listen for the /hbnb url. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def dynamic_url(text):
    """ Listen for /c/dynamic url. """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dynamic_url2(text='is cool'):
    """ Listen for /python/dynamic url. """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_url(n):
    """ Listen for a number url endpoints."""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
