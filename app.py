from flask import Flask

app = Flask("Hello")

@app.route("/")
def Hello():
    return "Agenda do Governo"

@app.route("/contatos")
def contato():
    return "Cesar Augusto Andrade Ferreira"

@app.route("/html")
def html():
    return """<html>
        <head>
            <title> Agenda Do Governo </title>
        </head>
        <body>
            <h1>Lista de Contatos das Entidades Administrativas do Estado do Amazonas</h1>
        </body>
    </html>
    """