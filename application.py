from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/present")
def present():
    return render_template("present.html")

@app.route("/past")
def past():
    return render_template("past.html")

@app.route("/future")
def future():
    return render_template("future.html")
    
