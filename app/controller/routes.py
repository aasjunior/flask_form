from flask import Flask, render_template

def init(app):
    @app.route("/")
    def index():
        return render_template("index.html", title="Pagina Inicial")
    
    @app.route("/pacientes/cadastro")
    def cadastro_paciente():
        return render_template("pages/pacientes/cadastro_paciente.html", title="Cadastro de Paciente")