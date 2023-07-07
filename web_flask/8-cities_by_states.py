#!/usr/bin/python3
"""module named 7-states_list"""
from flask import Flask, render_template
from models import storage, state, city


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_template():
    """displays a template with a fetched
    data from the storage engine"""
    state_list = storage.all(state.State).values()
    city_list = []
    for st in state_list:
        city_list.append(st.cities)
    return render_template("7-states_list.html",
                           title="States", states=state_list, cities=city_list)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
