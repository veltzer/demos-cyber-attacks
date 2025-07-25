""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "termcolor",
    "yattag",
    "flask",
    "flask-mysql",
    "Flask-Limiter",
    "scapy",
    "mysql.connector",
    "gevent",
    "dnslib",
    "pyslowloris",
    "pylogconf",
]
build_requires: list[str] = config.shared.BUILD
test_requires: list[str] = config.shared.TEST
types_requires: list[str] = [
    "types-termcolor",
    "types-requests",
]
requires = install_requires + build_requires + test_requires + types_requires
