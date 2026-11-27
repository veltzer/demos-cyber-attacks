#!/usr/bin/env python

"""
An example of an unrestricted file download
"""


import flask

ROOT = """
<html><body>
<a href="/download?file=file1.txt">get file1</a>
<a href="/download?file=file2.txt">get file2</a>
<a href="/download?file=file3.txt">get file3</a>
</body></html>
"""


app = flask.Flask("app")


@app.route("/")
def root() -> str:
    """ root url """
    return ROOT


@app.route("/download")
def add() -> str:
    file = flask.request.args.get("file", "")
    with open(file) as s:
        return s.read()


app.run(port=8080, host="0.0.0.0")
