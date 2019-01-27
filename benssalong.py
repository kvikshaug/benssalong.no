from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route("/")
def home():
    return render_template("home.html", page="home")


@app.route("/varetilbud")
def varetilbud():
    return render_template("varetilbud.html", page="varetilbud")


@app.route("/galleri")
def galleri():
    return render_template("galleri.html", page="galleri")


@app.route("/omoss")
def omoss():
    return render_template("omoss.html", page="omoss")


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", page="kontakt")
