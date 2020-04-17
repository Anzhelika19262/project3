from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, TextAreaField, StringField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    name = StringField('Your login', validators=[DataRequired()])
    country = StringField('Where are you from?', validators=[DataRequired()])
    native_language = StringField('What is your native language?', validators=[DataRequired()])
    new_language = StringField('What language would you like to study?', validators=[DataRequired()])
    about_yourself = TextAreaField("About yourself and your hobbies")
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    rules = BooleanField('Do you accept the rules?')
    submit = SubmitField('Enter')
