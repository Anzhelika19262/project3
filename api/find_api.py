import flask
from flask import render_template, abord
from data import db_session, users
from forms import find_form

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
        user = session.query(users.User).filter(users.User.country.like(f'%{form.country.data.strip()}%'),
                                                users.User.native_language.like(f'%{form.native_language.data.strip()}%'),
                                                users.User.new_language.like(f'%{form.new_language.data.strip()}%'),
                                                users.User.about_yourself.like(f"%{form.interests.data}%")).all()
        if user:
            return render_template('friends.html', title='people', users=user)
        else:
            abord(404)
    return render_template('find.html', title='Find friends', form=form)
