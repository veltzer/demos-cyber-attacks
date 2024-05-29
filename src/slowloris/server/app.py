#!/usr/bin/env python3

"""
Super simple web server
"""

from flask import Flask
from flask_limiter import Limiter


app = Flask("app")


@app.route("/")
@limiter.limit("5 per minute")  # Route-specific limit
def root():
    """ catch all urls """
    return "<html><body><h1>python with flask in a docker<h1></body><html>"


app.run(port=8080, host="0.0.0.0")
