from flask import Flask, render_template

def init(app):
    @app.route("/")
    def index():
        return render_template("index.html", title="Pagina Inicial")