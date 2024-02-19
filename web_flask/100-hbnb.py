#!/usr/bin/python3
"""_summary_
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


# Teardown method to remove the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


# Route for /hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a webpage similar to 8-index.html"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    places = sorted(storage.all(Place).values(), key=lambda p: p.name)

    return render_template(
        "100-hbnb.html", states=states, amenities=amenities, places=places
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
