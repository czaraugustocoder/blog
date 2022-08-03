from flask import Flask

app = Flask("Hello")

@app.route("/")
def Hello():
    return "Hello World"