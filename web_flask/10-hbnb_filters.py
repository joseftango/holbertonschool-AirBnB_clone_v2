#!/usr/bin/python3
'''0-hello_route Module'''
from flask import Flask, render_template
from models import storage
import models


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays html page"""
    states = storage.all(models.State).values()
    amenities = storage.all(models.Amenity).values()
    for a in amenities:
        print(a)
    return render_template('10-hbnb_filters.html', data={'states': states, 'amenities': amenities})


@app.teardown_appcontext
def close_session(exception=None):
    '''close session when app context is torn down'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
