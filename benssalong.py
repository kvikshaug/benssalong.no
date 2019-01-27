import os

from flask import Flask, redirect, render_template, request, session, url_for

import db


app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(32)
app.config['PASSWORD'] = os.environ['PASSWORD']


@app.route("/")
def home():
    return render_template("home.html", page="home", data=db.data)


@app.route("/varetilbud")
def varetilbud():
    return render_template("varetilbud.html", page="varetilbud", data=db.data)


@app.route("/galleri")
def galleri():
    return render_template("galleri.html", page="galleri", data=db.data)


@app.route("/omoss")
def omoss():
    return render_template("omoss.html", page="omoss", data=db.data)


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", page="kontakt", data=db.data)


@app.route("/login", methods=["GET", "POST"])
def login():
    if 'authenticated' in session:
        return redirect(url_for('admin'))
    failed_login = False
    if request.method == 'POST':
        if request.form.get('password', '') == app.config['PASSWORD']:
            session['authenticated'] = True
            return redirect(url_for('admin'))
        else:
            failed_login = True
    return render_template("login.html", page="login", data=db.data, failed_login=failed_login)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if 'authenticated' not in session:
        return redirect(url_for('login'))
    
    if request.method == "GET":
        return render_template("admin.html", page="admin", data=db.data_unescaped())
    else:
        db.save(
            åpningstider=request.form['åpningstider'],
            priser=request.form['priser'],
            timebestilling=request.form['timebestilling'],
            nyheter=request.form['nyheter'],
            varetilbud=request.form['varetilbud'],
        )
        return render_template("admin.html", page="admin", data=db.data_unescaped(), saved=True)


@app.route("/loggut")
def logout():
    session.pop('authenticated', None)
    return redirect(url_for('home'))
