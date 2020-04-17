import flask
from flask import render_template, redirect
from data import db_session, users
from forms import find_form
from flask_login import login_user

blueprint = flask.Blueprint('find_api', __name__,
                            template_folder='templates')


@blueprint.route('/find')
def find_all():
    session = db_session.create_session()
    user = session.query(users.User).all()
    return render_template('friends.html', title='people', users=user)


@blueprint.route('/find_new', methods=['GET', 'POST'])
def find_friend():
    form = find_form.FriendForm()
    session = db_session.create_session()
    if form.validate_on_submit():
        user = session.query(users.User).filter(users.User.name.like(f'%{form.person.data}%'),
                                                users.User.country.like(f'%{form.country.data}%'),
                                                users.User.native_language.like(f'%{form.native_language.data}%'),
                                                users.User.new_language.like(f'%{form.new_language.data}%'),
                                                form.interests.data in users.User.about_yourself).all()
        return render_template('friends.html', title='people', users=user)
    return render_template('find.html', title='Find friends', form=form)
