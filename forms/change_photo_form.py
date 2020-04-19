from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class PhotoForm(FlaskForm):
    new_image = FileField('Your photo:')
    submit = SubmitField('Change')