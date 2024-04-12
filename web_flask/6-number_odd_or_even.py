#!/usr/bin/python3
"""import"""
from flask import Flask, render_template


app = Flask(__name__)


"""decorate"""


@app.route('/', strict_slashes=False)
def hello():
    """return"""
    return "Hello HBNB!"


"""decorate"""


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


"""decorate"""


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """return"""
    text = text.replace("_", " ")
    return f"C {text}"


"""decorate"""


@app.route("/python/", defaults={"text": "is_cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """return"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


"""decorate"""


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return"""
    return f"{n} is a number"


"""decorate"""


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    """return"""
    return render_template("5-number.html", n=n)


"""decorate"""


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """conditional"""
    ev_od = ""
    if n % 2 == 1:
        """return"""
        ev_od = "odd"
        return render_template("6-number_odd_or_even.html", n=n, ev_od=ev_od)
    elif n % 2 == 0:
        """return"""
        ev_od = "even"
        return render_template("6-number_odd_or_even.html", n=n, ev_od=ev_od)


"""entry point"""
if __name__ == "__main__":
    """run flask"""
    app.run(host="0.0.0.0", port=5000)
