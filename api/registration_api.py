import flask
from flask import render_template, redirect
from data import db_session, users
from forms import log_in, register_form
from flask_login import login_user

blueprint = flask.Blueprint('registration_api', __name__,
                            template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = log_in.LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/Stories")
        return render_template('login.html',
                               message="Wrong login or password", title='Authorization',
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@blueprint.route('/register', methods=['GET', 'POST'])
def reqister():
    form = register_form.RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="Passwords don't match")
        session = db_session.create_session()
        if session.query(users.User).filter(users.User.email == form.email.data).first():
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="This user already exists")
        if session.query(users.User).filter(users.User.name == form.name.data).first():
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="Person with such login already exist")
        user = users.User(
            name=form.name.data,
            email=form.email.data,
            country= form.country.data,
            native_language=form.native_language.data,
            new_language=form.new_language.data,
            about_yourself=form.about_yourself.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Registration', form=form)
