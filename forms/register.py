from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField, BooleanField

class RegisterForm(FlaskForm):
    email = StringField('username', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=15)])
