from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, StringField, SubmitField


class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField("Content")
    language = StringField('Language')
    submit = SubmitField('Append')
