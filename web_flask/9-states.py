#!/usr/bin/python3
"""_summary_
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import models

app = Flask(__name__)


# Teardown method to remove the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


# Route for /states
@app.route("/states", strict_slashes=False)
def states():
    """Display a list of states and their cities"""
    pep_fix = models.all_classes["State"]
    data = storage.all(cls=pep_fix)
    states = data.values()
    return render_template("7-states_list.html", states_list=states)


# Route for /states/<id>
@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """Display a state and its cities by ID"""
    pep_fix = models.all_classes["State"]
    data = models.storage.all(cls=pep_fix)
    states = data.values()
    return render_template("8-cities_by_states.html", states_list=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
