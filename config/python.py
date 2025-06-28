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
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
    # types
    "types-termcolor",
]
requires = install_requires + build_requires + test_requires
