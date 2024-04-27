#!/usr/bin/env python3

"""
A web server suffering from injection problems
"""


import sys
import os
import requests
import flask
import mysql.connector


host=os.environ.get("env_db_host")
user=os.environ.get("env_db_user")
password=os.environ.get("env_db_password")
database=os.environ.get("env_db_name")
print(f"{host=}")
print(f"{user=}")
print(f"{password=}")
print(f"{database=}")
# Connect to the MySQL database
#mydb = mysql.connector.connect(
#  host=host,
#  user=user,
#  password=password,
#  database=database,
# )

# mydb.close()


ADDBOOK = """
<html><body>
<form action="/addsubmit" method="get">
<label for="name">Name:</label>
<input type="text" id="name" name="name"></input><br><br>
<label for="year">Year:</label>
<input type="text" id="year" name="year"></input><br><br>
<input type="submit" value="Add the book">
</form>
</body></html>
"""

ROOT = """
<html><body>
    <a href="addbook">Add a book</a>
    <a href="listbooks">List books</a>
</body></html>
"""

ADDSUMBIT = """
<html><body>
    <a href="">Go to main menu</a>
</body></html>
"""



app = flask.Flask("app")


@app.route("/")
def root():
    return ROOT


@app.route("/listbooks")
def listbooks():
    """ This will list all books in the database """
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM books")
    rows = mycursor.fetchall()
    mycursor.close()
    return "</br>".join(rows)

@app.route("/addbook")
def addbook():
    """ This will show a form to add a single book to the database """
    return ADDBOOK


@app.route("/addsubmit")
def addsubmit():
    """ This will get the data for the new book and insert it into the database """
    return ADDSUMBIT


port = int(os.environ.get("env_app_port"))
host = os.environ.get("env_app_host")
app.run(port=port, host=host)
