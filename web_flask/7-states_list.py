#!/usr/bin/python3
"""_summary_
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


# Route for /states_list
@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a list of states from DBStorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template("7-states_list.html", states=sorted_states)


# Teardown method to remove the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
