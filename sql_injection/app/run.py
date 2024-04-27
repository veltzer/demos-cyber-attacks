#!/usr/bin/env python

"""
Run the app in gunicorn or flask
"""

import os
import subprocess

GUNICORN=False

if GUNICORN:
    env_app_port = int(os.environ.get("env_app_port"))
    env_app_listen = os.environ.get("env_app_listen")
    print(f"{env_app_port=}")
    print(f"{env_app_listen=}")
    subprocess.check_call([
        "gunicorn",
        "--config",
        "gunicorn_conf.py",
        "--bind",
        f"{env_app_listen}:{env_app_port}",
        "wsgi:app",
    ])
else:
    subprocess.check_call([
        "/app.py"
    ])
