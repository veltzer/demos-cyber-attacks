#!/usr/bin/env python

import os
import subprocess

env_app_port = int(os.environ.get("env_app_port"))
env_app_listen = os.environ.get("env_app_listen")
print(f"{env_app_port=}")
print(f"{env_app_listen=}")
subprocess.check_call([
    "gunicorn",
    "--bind",
    f"{env_app_listen}:{env_app_port}",
    "wsgi:app",
])
