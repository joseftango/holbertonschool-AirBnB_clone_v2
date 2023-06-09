#!/usr/bin/python3
"""9-states Module"""
from flask import Flask, render_template
from models import storage
from models.place import Place
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove SQLAlchemy Session"""
    storage.close()

@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Displays templates"""
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    states = storage.all(State).values()
    my_cities = list()

    for state in states:
        for city in state.cities:
            my_cities.append(city)

    return render_template('100-hbnb.html',
                           my_states=states, my_cities=my_cities,
                           my_amenities=amenities, my_places=places)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
