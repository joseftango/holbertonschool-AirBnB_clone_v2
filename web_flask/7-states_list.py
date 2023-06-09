#!/usr/bin/python3
"""module named 7-states_list"""
from flask import Flask, render_template
from models import storage, state


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Displays html page"""
    states = storage.all(state.State).values()
    return render_template('7-states_list.html', my_dict=states)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
