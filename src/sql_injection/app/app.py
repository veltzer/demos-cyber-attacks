#!/usr/bin/env python3

"""
A web server suffering from injection problems
"""


import os
import logging
import flask
from flask import request
# from sqlalchemy import create_engine
import mysql.connector
from yattag import Doc, indent


host = os.environ["env_db_host"]
user = os.environ["env_db_user"]
password = os.environ["env_db_password"]
database = os.environ["env_db_name"]
print(f"{host=}")
print(f"{user=}")
print(f"{password=}")
print(f"{database=}")

# create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def get_connection():
    """ get a fresh connection to the database """
    connection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database,
    )
    return connection


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


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["MYSQL_DATABASE_HOST"] = host
app.config["MYSQL_DATABASE_USER"] = user
app.config["MYSQL_DATABASE_PASSWORD"] = password
app.config["MYSQL_DATABASE_DB"] = database
app.config["MYSQL_POOL_SIZE"] = 10
uri = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
app.config["SQLALCHEMY_DATABASE_URI"] = uri
# Optional: Set pool size (default 5)
app.config["SQLALCHEMY_POOL_SIZE"] = 20
# Optional: Set pool recycle time (default None)
app.config["SQLALCHEMY_POOL_RECYCLE"] = 300
# db = SQLAlchemy(app)
# pool = MySQL(app)
# engine = create_engine(uri)


@app.route("/")
def index():
    """ main route """
    return app.send_static_file("index.html")


@app.route("/listbooks")
def listbooks():
    """ This will list all books in the database """
    with get_connection() as conn:
        return describe_table_data_html(conn, "books")


@app.route("/reset")
def reset():
    """ This will recreate the database """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "sql/reset.sql")
    with open(file_path, "r", encoding="utf8") as file:
        contents = file.read()
    with get_connection() as conn:
        with conn.cursor() as cursor:
            conn.start_transaction()
            iterator = cursor.execute(contents, multi=True)
            for _ in iterator:
                pass
            conn.commit()
    return "OK"


@app.route("/addbook")
def addbook():
    """ This will add a new book to the database """
    with get_connection() as conn:
        # Get book details from the request
        title = request.args.get("title")
        author = request.args.get("author")
        genre = request.args.get("genre")
        year = request.args.get("year")
        safe = request.args.get("safe")

        with conn.cursor() as cursor:
            conn.start_transaction()
            if safe:
                query = "INSERT INTO books (title, author, genre, year) \
                        VALUES (%s, %s, %s, %s)"
                values = (title, author, genre, year)
                iterator = cursor.execute(query, values)
                for _ in iterator:
                    pass
            else:
                query = f"INSERT INTO books (title, author, genre, year) \
                    VALUES (\"{title}\", \"{author}\", \"{genre}\", {year})"
                logger.debug(query)
                iterator = cursor.execute(query, multi=True)
                for _ in iterator:
                    pass
            conn.commit()
        return "Book added successfully"


if __name__ == "__main__":
    port = int(os.environ["env_app_port"])
    listen = os.environ["env_app_listen"]
    print(f"{port=}")
    print(f"{listen=}")
    app.run(port=port, host=listen, debug=True)
