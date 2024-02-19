#!/usr/bin/python3
"""_summary_
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


# Route for /cities_by_states
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a list of states and their associated cities"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template("8-cities_by_states.html", states=sorted_states)


# Teardown method to remove the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
