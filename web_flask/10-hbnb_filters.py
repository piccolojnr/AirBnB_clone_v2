#!/usr/bin/python3
"""_summary_
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


# Teardown method to remove the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


# Route for /hbnb_filters
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a webpage similar to 6-index.html"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
