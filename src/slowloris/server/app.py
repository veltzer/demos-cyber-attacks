#!/usr/bin/env python

"""
Super simple web server
"""

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask("app")
# limiter = Limiter(app)  # noqa: ERA001  teaching: kept in the comment for the reader
limiter = Limiter(
    key_func=get_remote_address,  # Limit by IP address
    # app,
    # default_limits=["200 per day", "50 per hour"]  # Global limits  # noqa: ERA001  teaching: kept in the comment for the reader
)


@app.route("/")
@limiter.limit("500/minute")
def root() -> str:
    """ catch all urls """
    return "<html><body><h1>python with flask in a docker<h1></body><html>"


app.run(port=8080, host="0.0.0.0")
