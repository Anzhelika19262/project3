from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Markform(FlaskForm):
    coords = StringField("Your location:")
    submit = SubmitField('Send')