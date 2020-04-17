from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Enter')
