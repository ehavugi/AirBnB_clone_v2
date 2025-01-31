#!/usr/bin/python3
"""
Hello world
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hnb():
    """Route server for /hbnb
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
