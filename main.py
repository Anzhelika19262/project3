import os
from flask import Flask, render_template
from data import db_session, users
from flask_login import LoginManager
from api import news_api, registration_api, find_api, messagers_api, profile_api, map_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(users.User).get(user_id)


def main():
    app.register_blueprint(find_api.blueprint)
    app.register_blueprint(registration_api.blueprint)
    app.register_blueprint(news_api.blueprint)
    app.register_blueprint(messagers_api.blueprint)
    app.register_blueprint(profile_api.blueprint)
    app.register_blueprint(map_api.blueprint)
    db_session.global_init("db/all_users.sqlite")


@app.route("/")
@app.route("/main_page")
def main_page():
    return render_template('main_page.html', title='Welcome')


if __name__ == '__main__':
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
