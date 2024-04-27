#!/usr/bin/env python3

"""
A web server suffering from injection problems
"""


import os
import flask
import mysql.connector
from yattag import Doc, indent


DO_MYSQL = True
host = os.environ.get("env_db_host")
user = os.environ.get("env_db_user")
password = os.environ.get("env_db_password")
database = os.environ.get("env_db_name")
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


def describe_table_data(conn, table_name):
    """
    This function describes all data in a MySQL table and
    returns a string.
    Args:
      conn: A MySQL connection object.
      table_name: The name of the table to describe.
    Returns:
      A string describing the table data, including column names and rows.
    Raises:
      mysql.connector.Error: If there is an error connecting to the
      database or executing the query.
    """
    try:
        cursor = conn.cursor()
        # Get table schema (column names and data types)
        cursor.execute(f"DESCRIBE {table_name}")
        column_descriptions = cursor.fetchall()
        # Build the description string header with column names
        description_str = " | ".join([f"{col[0]}" for col in
                                      column_descriptions]) + "\n"
        description_str += "-" * len(description_str) + "\n"
        # Fetch table data (rows)
        cursor.execute(f"SELECT * FROM {table_name}")
        table_data = cursor.fetchall()
        # Add each row of data to the description string
        for row in table_data:
            formatted_row = [str(val) for val in row]
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
      A string containing HTML code representing the table
      data with a basic styling.
    Raises:
      mysql.connector.Error: If there is an error connecting
      to the database or executing the query.
    """
    try:
        cursor = conn.cursor()
        # Get table schema (column names and data types)
        cursor.execute(f"DESCRIBE {table_name}")
        column_descriptions = cursor.fetchall()

        # Build the HTML table header row
        doc, tag, text = Doc().tagtext()
        with tag("html"):
            with tag("body"):
                with tag("table"):
                    with tag("tr"):
                        with tag("th"):
                            pass
                        for col in column_descriptions:
                            with tag("th"):
                                text(str(col[0]))
                    cursor.execute(f"SELECT * FROM {table_name}")
                    table_data = cursor.fetchall()
                    for row in table_data:
                        with tag("tr"):
                            with tag("td"):
                                pass
                            for val in row:
                                with tag("td"):
                                    text(str(val))
                with tag("buttom"):
                    with tag("a", href="/"):
                        text("Back to index")
        pretty_html = indent(doc.getvalue())
        return pretty_html
        # return doc.getvalue()

    except mysql.connector.Error as err:
        raise err  # Re-raise the error for handling


app = flask.Flask("app")
app.config["DEBUG"] = True


@app.route("/")
def index():
    """ main route """
    return app.send_static_file("index.html")


@app.route("/listbooks")
def listbooks():
    """ This will list all books in the database """
    return describe_table_data_html(mydb, "books")


if __name__ == "__main__":
    port = int(os.environ["env_app_port"])
    listen = os.environ.get("env_app_listen")
    print(f"{port=}")
    print(f"{listen=}")
    app.run(port=port, host=listen)
