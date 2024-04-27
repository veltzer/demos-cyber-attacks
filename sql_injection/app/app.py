#!/usr/bin/env python3

"""
A web server suffering from injection problems
"""


import sys
import os
import requests
import flask
import mysql.connector


DO_MYSQL=True
host=os.environ.get("env_db_host")
user=os.environ.get("env_db_user")
password=os.environ.get("env_db_password")
database=os.environ.get("env_db_name")
print(f"{host=}")
print(f"{user=}")
print(f"{password=}")
print(f"{database=}")
# Connect to the MySQL database
if DO_MYSQL:
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )

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

def describe_table_data(conn, table_name):
  """
  This function describes all data in a MySQL table and returns a string.

  Args:
      conn: A MySQL connection object.
      table_name: The name of the table to describe.

  Returns:
      A string describing the table data, including column names and rows.

  Raises:
      mysql.connector.Error: If there is an error connecting to the database or executing the query.
  """
  try:
    cursor = conn.cursor()

    # Get table schema (column names and data types)
    cursor.execute(f"DESCRIBE {table_name}")
    column_descriptions = cursor.fetchall()

    # Build the description string header with column names
    description_str = " | ".join([f"{col[0]}" for col in column_descriptions]) + "\n"
    description_str += "-" * len(description_str) + "\n"

    # Fetch table data (rows)
    cursor.execute(f"SELECT * FROM {table_name}")
    table_data = cursor.fetchall()

    # Add each row of data to the description string
    for row in table_data:
      formatted_row = [str(val) for val in row]  # Convert all values to strings
      description_str += " | ".join(formatted_row) + "\n"

    return description_str

  except mysql.connector.Error as err:
    raise err  # Re-raise the error for handling


def describe_table_data_html(conn, table_name):
  """
  This function describes all data in a MySQL table and returns HTML code.

  Args:
      conn: A MySQL connection object.
      table_name: The name of the table to describe.

  Returns:
      A string containing HTML code representing the table data with a basic styling.

  Raises:
      mysql.connector.Error: If there is an error connecting to the database or executing the query.
  """
  try:
    cursor = conn.cursor()

    # Get table schema (column names and data types)
    cursor.execute(f"DESCRIBE {table_name}")
    column_descriptions = cursor.fetchall()

    # Build the HTML table header row
    html_str = "<table>\n  <tr>\n"
    html_str += "    <th>" + "</th>\n    <th>".join([f"{col[0]}" for col in column_descriptions]) + "</th>\n  </tr>\n"

    # Fetch table data (rows)
    cursor.execute(f"SELECT * FROM {table_name}")
    table_data = cursor.fetchall()

    # Add each row of data to the HTML table
    for row in table_data:
      html_str += "  <tr>\n"
      html_str += "    <td></td>\n    <td>" + "</td>\n    <td>".join([str(val) for val in row]) + "</td>\n  </tr>\n"

    html_str += "</table>\n"
    html_str += "<button><a href=\"/\">Back to index</a></button>"
    return html_str

  except mysql.connector.Error as err:
    raise err  # Re-raise the error for handling


app = flask.Flask("app")
app.config['DEBUG'] = True

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/listbooks")
def listbooks():
    """ This will list all books in the database """
    return describe_table_data_html(mydb, "books")

@app.route("/addbook")
def addbook():
    """ This will show a form to add a single book to the database """
    return ADDBOOK


@app.route("/addsubmit")
def addsubmit():
    """ This will get the data for the new book and insert it into the database """
    return ADDSUMBIT


if __name__ == "__main__":
    port = int(os.environ.get("env_app_port"))
    listen = os.environ.get("env_app_listen")
    print(f"{port=}")
    print(f"{listen=}")
    app.run(port=port, host=listen)
