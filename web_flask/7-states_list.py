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


@app.route("/states_list", strict_slashes=False)
def states_listing():
    all_states = list(storage.all("State").values())
    all_states.sort(key=get_name)
    return render_template("7-states_list.html", states=all_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current db session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
