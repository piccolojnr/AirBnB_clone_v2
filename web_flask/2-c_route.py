#!/usr/bin/python3
"""_summary_
"""
from flask import Flask, render_template

app = Flask(__name__)


# Route for the home page
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "Hello HBNB!"


# Route for /hbnb
@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "HBNB"


# Route for /c/<text>
@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """_summary_

    Returns:
        _type_: _description_
    """
    # Replace underscore _ symbols with a space
    formatted_text = text.replace("_", " ")
    return "C {}".format(formatted_text)


if __name__ == "__main__":
    # Run the application on 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
