#!/usr/bin/python3
"""Import required modules"""
from markupsafe import escape
from flask import Flask, url_for, request

app = Flask(__name__)

"""decorator to direct Flask which URL to display for the function"""
@app.route("/<name>")
def admin_world(name):
    return ("Hello {}".format(escape(name)))

@app.route("/")
def greet_user():
    return "<p>Hello User</p>"

@app.route("/name/<username>")
def username(username):
    return ("Hello {}".format(escape(username)))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST method used"
    else:
        return "GET method used"


if __name__ == "__main__":
    app.run(debug=True)
