from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField, PasswordField, validators

class PalabraForm(Form):

    ingles = StringField("Ingles: ",[validators.DataRequired(message="Se requiere poner texto")])
    espaniol = StringField("Español: ",[validators.DataRequired(message="Se requiere poner texto")])
    palabra = StringField("Palabra: ")
    