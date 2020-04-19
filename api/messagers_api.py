import flask
from flask import render_template, redirect
from data import db_session, users, message, friends
from forms import message_form
from flask_login import login_required, current_user

blueprint = flask.Blueprint('messagers_api', __name__, template_folder='templates')


@blueprint.route('/messager/<int:id>', methods=['GET', 'POST'])
def new_chat(id):
    session = db_session.create_session()
    interlocutor = session.query(users.User).filter(users.User.id == id).first().name
    user = current_user.name
    names = '_'.join(sorted([user, interlocutor]))
    form = message_form.MessageForm()
    if form.validate_on_submit():
        new_dialog = message.Message()
        new_dialog.names = names
        new_dialog.message = form.messages.data
        new_dialog.from_who = user
        session.add(new_dialog)
        session.commit()
    messages = session.query(message.Message).filter(message.Message.names == names).all()
    if session.query(friends.Friend).filter(friends.Friend.friend_name == interlocutor,
                                            friends.Friend.user_name == user).first() is None:
        add_friend_user(user, interlocutor)
        add_friend_interlocutor(interlocutor, user)
    if messages is not None:
        return render_template('messages.html', title='messages', form=form, previous_sms=messages)
    return render_template('messages.html', title='messages', form=form, previous_sms='')


def add_friend_user(user, new_user_friend):
    session = db_session.create_session()
    new_friend = friends.Friend()
    new_friend.user_name = user
    new_friend.friend_name = new_user_friend
    session.add(new_friend)
    session.commit()


def add_friend_interlocutor(interlocator, user):
    session = db_session.create_session()
    user_friend = friends.Friend()
    user_friend.user_name = interlocator
    user_friend.friend_name = user
    session.add(user_friend)
    session.commit()


@blueprint.route('/Message', methods=['GET'])
@login_required
def user_interlocutors():
    session = db_session.create_session()
    all_interlocutors = session.query(friends.Friend).filter(friends.Friend.user_name == current_user.name).all()
    if all_interlocutors is not None:
        return render_template('all_interlocutors.html', title='Friends', friends=all_interlocutors)
    return render_template('all_interlocutors.html', title='Friends', friends='')
