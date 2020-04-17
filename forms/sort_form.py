from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SortForm(FlaskForm):
    language_sort = StringField("What language would you like to read story on?")
    submit = SubmitField('Find')