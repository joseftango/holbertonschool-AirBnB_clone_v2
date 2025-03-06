#!/usr/bin/python3
'''0-hello_route Module'''
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    """Displays html page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_states(id=None):
    '''displays states and everyone
    with it linked cities after'''
    states = storage.all(State).values()
    my_state = None
    for state in states:
        if state.id == id:
            my_state = state
            break
    return render_template('9-states.html', my_state=my_state)


@app.teardown_appcontext
def close_session(exception=None):
    '''close session when app context is torn down'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
