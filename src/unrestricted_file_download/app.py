"""
This application demonstrates the unrestricted file download vulnerability
"""

from flask import Flask, send_file

app = Flask("app")


@app.route("/download")
def download():
    """ This is the vulnerability route """
    try:
        filename = "your_file.pdf"
        return send_file(
                filename,
                mimetype="application/pdf",
                as_attachment=True,
        )
    except FileNotFoundError:
        return "File Not Found", 404


if __name__ == "__main__":
    app.run(debug=True)
