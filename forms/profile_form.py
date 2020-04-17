from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.fields.html5 import EmailField


class ProfileForm(FlaskForm):
    new_language = StringField('Target language')
    about_yourself = TextAreaField('About yourself')
    email = EmailField('Your email')
    submit = SubmitField('Change')
