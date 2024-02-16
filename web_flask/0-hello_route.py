#!/usr/bin/python3
# This is the app.py module for this flask project

from flask import Flask
# Import the flask class from its module


app = Flask(__name__)
# Instantiate/create a flask app


@app.route('/', strict_slashes=False)
def hello():
    """ Listen/link to the home url """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """ Disallow importing and running app.py as a module """
    app.run(host='0.0.0.0', port=5000)
