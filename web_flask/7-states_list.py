#!/usr/bin/python3
"""module named 7-states_list"""
from flask import Flask, render_template
from models import storage, state


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_template():
    """displays a template with a fetched
    data from the storage engine"""
    state_list = storage.all(state.State).values()
    return render_template("7-states_list.html",
                           title="States", states=state_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
