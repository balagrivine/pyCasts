#!/usr/bin/python3
"""Import required modules"""
from markupsafe import escape
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def greet_user():
    return "<p>Hello User</p>"

@app.route("/<name>/<username>")
def username(name, username):
    return ("Hello {} {}".format(escape(username), escape(name)))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('app.html')
    else:
        return login_get()
@app.get('/login')
def login_get():
    return "Get method used"
@app.post('/login')
def login_post():
    return "POST method used"
if __name__ == "__main__":
    app.run(debug=True)
