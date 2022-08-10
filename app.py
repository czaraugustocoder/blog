from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
def Hello():
    return "Agenda do Governo"

@app.route("/contatos")
def contato():
    return "Cesar Augusto Andrade Ferreira"

@app.route("/html")
def html():
    return render_template("index.html")