from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp

regex = {
    'email': r'^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$',
    'cpf': r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    'telefone': r'^\(\d{2}\) \d{5}-\d{4}$'
}

class PacienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35), Regexp(regex['email'])])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(min=10, max=15), Regexp(regex['telefone'])])
    cpf = StringField('CPF', validators=[DataRequired(), Regexp(regex['cpf'])])
    nascimento = StringField('Nascimento', validators=[DataRequired()])
    uf = StringField('UF', validators=[DataRequired(), Length(min=2, max=2)])