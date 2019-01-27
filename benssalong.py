from flask import Flask, render_template

from db import data


app = Flask(__name__)
app.debug = True


@app.route("/")
def home():
    return render_template("home.html", page="home", data=data)


@app.route("/varetilbud")
def varetilbud():
    return render_template("varetilbud.html", page="varetilbud", data=data)


@app.route("/galleri")
def galleri():
    return render_template("galleri.html", page="galleri", data=data)


@app.route("/omoss")
def omoss():
    return render_template("omoss.html", page="omoss", data=data)


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", page="kontakt", data=data)
