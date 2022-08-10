from flask import Flask

app = Flask("Hello")

@app.route("/")
def Hello():
    return "Agenda do Governo"

@app.route("/contatos")
def contato():
    return "Cesar Augusto Andrade Ferreira"