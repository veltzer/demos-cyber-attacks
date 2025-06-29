""" python deps for this project """

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
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
    "pycmdtools",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
    # types
    "types-termcolor",
    "types-requests",
]
requires = install_requires + build_requires + test_requires
