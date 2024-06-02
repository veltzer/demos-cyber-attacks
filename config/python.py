from typing import List


dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "termcolor",
    "yattag",
    "flask",
    "flask-mysql",
    "Flask-Limiter",
    "scapy",
    "mysql.connector",
    "gevent",
    "dnslib",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pycmdtools",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pyflakes",
    "mypy",
    "pylogconf",
    "types-termcolor",
    "types-PyYAML",
]
requires = config_requires + install_requires + build_requires + test_requires
