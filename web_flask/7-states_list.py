#!/usr/bin/python3
"""
Hello world
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

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


@app.route("/c/<text>", strict_slashes=False)
def textme(text):
    """Handle dynamic routes
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoncool(text="is cool"):
    """Handle python is cool!
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def routeInt(n):
    """Routes only for integer n otherwise 404 error
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def renderInt(n):
    """Render an integer using templates
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n):
    """Render int and whether it is odd or even using templates
    """
    return render_template("6-number_odd_or_even.html", n=n)


@app.route("/states_list", strict_slashes = False)
def states_listing():
    all_states = storage.all("State").values()
    return render_template("7-states_list.html", states=all_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current db session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
