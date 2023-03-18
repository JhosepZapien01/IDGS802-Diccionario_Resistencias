from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField, PasswordField, validators

def mi_validacion(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError("Las cajas de texto no pueden ir vacias")


class UserForm(Form):

    Matricula = StringField('Matricula',[validators.DataRequired(message="La matricula es un campo obligatorio")])
    Nombre=StringField('Nombre',[validators.DataRequired(message="Es necesario llenar el campo"),
                                 validators.length(min=5,max=15, message="Limites de caracteres")])
    ApePaterno=StringField('Apellido paterno',[mi_validacion])
    ApeMaterno=StringField('Apellido materno')
    Email=EmailField('Correo')

class Login(Form):
    Usuario = StringField('usuario',[validators.DataRequired(message="Es necesario tener un usuario")]) 
    Contrasenia = PasswordField('contraseña',[validators.DataRequired(message="Campo obligatorio"), validators.length(min=5,max=15,message="Ingresa un valor maximo")])