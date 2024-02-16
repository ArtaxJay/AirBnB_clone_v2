#!/usr/bin/python3
# This is the app.py module for this flask project

# Import the flask class from its module
from flask import Flask


# Instantiate/create a flask app
app = Flask(__name__)


# Listen/link to the home url
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Disallow importing and running app.py as a module
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
