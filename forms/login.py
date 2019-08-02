from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email
from wtforms import StringField, PasswordField, BooleanField

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(),Email(message='Invalid Email'), Length(min=4, max=40)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=15)])
    remember = BooleanField('remember me')
