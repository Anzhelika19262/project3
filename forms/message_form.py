from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class MessageForm(FlaskForm):
    messages = TextAreaField("Your message:")
    submit = SubmitField('Send')