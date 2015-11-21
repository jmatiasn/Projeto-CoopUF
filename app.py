__author__ = 'Joao'

from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/home")
def hello():
    return render_template("home.html")

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/publicacao")
def publicacao():
    return render_template("publicacao.html")

if __name__ == "__main__":
    app.run()