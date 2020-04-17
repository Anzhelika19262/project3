from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField


class FriendForm(FlaskForm):
    person = StringField('Person')
    country = StringField('Country')
    native_language = StringField('Native language')
    new_language = StringField('Target language')
    interests = TextAreaField('Interests')
    submit = SubmitField('Find')