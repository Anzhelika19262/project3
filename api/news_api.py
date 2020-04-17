import flask
from flask import render_template, redirect, abort
from data import db_session, news
from flask_login import login_required, current_user
from forms import news_form, sort_form

blueprint = flask.Blueprint('news_api', __name__,
                            template_folder='templates')


@blueprint.route("/Stories")
def index():
    session = db_session.create_session()
    new = session.query(news.News).all()
    return render_template("moments.html", title='story', news=new)


@blueprint.route('/add_news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = news_form.NewsForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        new = news.News()
        new.title = form.title.data
        new.content = form.content.data
        new.language = form.language.data
        current_user.news.append(new)
        session.merge(current_user)
        session.commit()
        return redirect('/Stories')
    return render_template('news.html', title='Add story',
                           form=form)


@blueprint.route('/news/<int:id>', methods=['GET'])
@login_required
def get_news(id):
    form = news_form.NewsForm()
    session = db_session.create_session()
    new = session.query(news.News).filter(news.News.id == id,
                                          news.News.user == current_user).first()
    if new:
        form.title.data = new.title
        form.content.data = new.content
        form.language.data = new.language
    else:
        abort(404)
    return render_template('news.html', title='Edit story', form=form)


@blueprint.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = news_form.NewsForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        new = session.query(news.News).filter(news.News.id == id, news.News.user == current_user).first()
        if new:
            new.title = form.title.data
            new.content = form.content.data
            new.language = form.language.data
            session.commit()
            return redirect('/Stories')
        else:
            abort(404)
    return render_template('news.html', title='Edit story', form=form)


@blueprint.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    session = db_session.create_session()
    new = session.query(news.News).filter(news.News.id == id,
                                          news.News.user == current_user).first()
    if new:
        session.delete(new)
        session.commit()
    else:
        abort(404)
    return redirect('/Stories')


@blueprint.route('/sort_news', methods=['GET', 'POST'])
def sort_news():
    form = sort_form.SortForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        new = session.query(news.News).filter(news.News.language.like(f'%{form.language_sort.data}%')).all()
        if new:
            return render_template("moments.html", title='story', news=new)
        else:
            abort(404)
    return render_template('sort_story.html', title='Sort', form=form)

