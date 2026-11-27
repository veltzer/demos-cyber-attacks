#!/usr/bin/env python

"""
Web server that can add two numbers
"""


import html
from typing import TYPE_CHECKING

import flask

if TYPE_CHECKING:
    from werkzeug.wrappers.response import Response

FORM = """
<html>
    <body>
        <form action="/add" method="post">
            <label for="value">value:</label>
            <textarea id="value" name="value" rows="10" cols="60"></textarea>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

ROOT = """
<!DOCTYPE html>
  <html>
    <body>
      Welcome to our chat!</br>
      <a href="comment">Add a comment</a>
      <a href="view">View Chat</a>
  </body>
</html>
"""


app = flask.Flask("app")


@app.route("/")
def root() -> str:
    """ root url """
    return ROOT


@app.route("/comment")
def comment() -> str:
    """ comment url """
    return FORM


@app.route("/view")
def view() -> str:
    """ view url """
    val = "<html><body>This is the view:"
    with open("chat.txt") as stream:
        val += stream.read()
    val += "</body></html>"
    return val


@app.route("/add", methods=["POST"])
def add() -> Response:
    """ this will add two numbers given to it """
    value = flask.request.form.get("value")
    value = html.escape(value or "")
    with open("chat.txt", "a") as stream:
        stream.write("<br/>")
        stream.write(value)
        stream.write("<br/>")
    return flask.redirect("/")


app.run(port=8080, host="0.0.0.0")
