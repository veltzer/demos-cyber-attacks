#!/usr/bin/env python

"""
Run the app in gunicorn or flask
"""

import os
import subprocess

GUNICORN = False

if GUNICORN:
    ENV_APP_PORT = int(os.environ["ENV_APP_PORT"])
    ENV_APP_LISTEN = os.environ.get("ENV_APP_LISTEN")
    print(f"{ENV_APP_PORT=}")
    print(f"{ENV_APP_LISTEN=}")
    subprocess.check_call([
        "gunicorn",
        "--config",
        "gunicorn_conf.py",
        "--bind",
        f"{ENV_APP_LISTEN}:{ENV_APP_PORT}",
        "wsgi:app",
    ])
else:
    subprocess.check_call([
        "/app.py"
    ])
