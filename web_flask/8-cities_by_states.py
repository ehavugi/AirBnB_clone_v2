#!/usr/bin/python3
"""
Hello world
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


def get_name(value):
    """get Name of the attribute
    """
    return value.name


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    all_states = list(storage.all("State").values())
    all_states.sort(key=get_name)
    return render_template("8-cities_by_states.html", states=all_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current db session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
