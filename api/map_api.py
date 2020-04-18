import flask
import requests
from flask import render_template, redirect, abort
from forms import mark_form
from data import db_session, map_pt

blueprint = flask.Blueprint('map_api', __name__, template_folder='templates')


@blueprint.route('/map', methods=['GET', 'POST'])
def show_map():
    form = mark_form.Markform()
    if form.validate_on_submit():
        new_mark = cheek_request(form.coords.data)
        create_pt(new_mark)
        response_pt()
        return redirect('/Stories')
    return render_template('map.html', form=form)


def cheek_request(request):
    toponym_to_find = request
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        abort(404)
    json_response = response.json()
    toponym_coodrinates = ','.join(json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["Point"]["pos"].split())
    return toponym_coodrinates


def create_pt(coords):
    new_pt = f'{coords},pm2dgm'
    session = db_session.create_session()
    new_mark = map_pt.Map_pt()
    new_mark.coord_pt = new_pt
    session.add(new_mark)
    session.commit()


def response_pt():
    session = db_session.create_session()
    list_pt = []
    all_pt = session.query(map_pt.Map_pt).all()
    for item in all_pt:
        list_pt.append(item.coord_pt)
    get_response(list_pt)


def get_response(list_pt):
    api_server = "http://static-maps.yandex.ru/1.x/"
    params = {
        "ll": "38.841371,45.775550",
        "l": "map",
        'z': '1',
        'size': '650,400',
        'pt': '~'.join(list_pt)
    }
    response = requests.get(api_server, params=params)
    map_file = 'static/img/map.jpg'
    with open(map_file, "wb") as file:
        file.write(response.content)


