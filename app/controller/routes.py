from flask import Flask, render_template, request, jsonify
from service.services import create_paciente
from model.schemas import PacienteForm

def init(app):
    @app.route("/")
    def index():
        return render_template("index.html", title="Pagina Inicial")
    
    @app.route("/pacientes/cadastro", methods=['GET', 'POST'])
    def cadastro_paciente():
        form = PacienteForm()

        if request.method == 'POST':
            success, result = create_paciente(request.form)

            if success:
                return jsonify(success=True)
            else:
                return jsonify(success=False, error=result)

        else:
            return render_template("pages/pacientes/cadastro_paciente.html", title="Cadastro de Paciente", form=form)