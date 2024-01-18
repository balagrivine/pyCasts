#!/usr/bin/python3
"""Import required modules"""
from markupsafe import escape
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/<name>/<username>")
def username(name, username):
    return ("Hello {} {}".format(escape(username), escape(name)))

def login_post():
    return render_template('survey.html')
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_post()
    return login_get()

def login_get():
    return render_template('survey.html')

if __name__ == "__main__":
    app.run(debug=True)
