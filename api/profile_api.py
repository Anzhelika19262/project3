import flask
from flask import render_template, redirect, abort, request
from data import db_session, users
from flask_login import login_required, current_user
from forms import profile_form

blueprint = flask.Blueprint('profile_api', __name__, template_folder='templates')


@blueprint.route('/profile')
@login_required
def user_page():
    session = db_session.create_session()
    inform_about_user = session.query(users.User).filter(users.User.id == current_user.id).first()
    return render_template('profile.html', inform_about_user=inform_about_user)


@blueprint.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    session = db_session.create_session()
    form = profile_form.ProfileForm()
    if form.validate_on_submit():
        user = session.query(users.User).filter(users.User.name == current_user.name).first()
        if user:
            user.new_language = form.new_language.data
            user.about_yourself = form.about_yourself.data
            user.email = form.email.data
            session.commit()
            return redirect('/profile')
        else:
            abort(404)
    return render_template('edit_profile.html', title='Edit profile', form=form)


@blueprint.route('/profile/<int:id>', methods=['GET'])
@login_required
def get_profile():
    form = profile_form.ProfileForm()
    session = db_session.create_session()
    user = session.query(users.User).filter(users.User == current_user).first()
    if user:
        form.new_language.data = user.new_language
        form.about_yourself.data = user.about_yourself
        form.email.data = user.email
    else:
        abort(404)
    return render_template('edit_profile.html', title='Edit profile', form=form)


@blueprint.route('/change_photo', methods=['GET', 'POST'])
def change_photo():
    session = db_session.create_session()
    user = session.query(users.User).filter(users.User.name == current_user.name).first()
    if user:
        if user.photo:
            photo = 'True'
    if request.method == 'POST':
        if user:
            user.photo = True
            session.commit()
            img = request.files['file']
            with open(f'static/img/{current_user.name}.jpg', 'wb') as new_photo:
                new_photo.write(img.read())
            return redirect('/Stories')
        else:
            abort(404)
    return render_template('change_photo.html', title='Edit profile', photo='True')