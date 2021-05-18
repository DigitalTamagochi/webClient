from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, make_response
from ..config import jest_list_url, API_SECRET_KEY
import requests


mainPage = Blueprint('mainPage', __name__)


def try_get_jest_list(user_login, user_token):
    params = dict(
        API_KEY = API_SECRET_KEY,
        QUERY = "GET_JEST_LIST",

        LOGIN=user_login,
        TOKEN=user_token
    )

    res = requests.post(jest_list_url, data=params)

    if res is None:
        # print("> Something gone wrong, server does not respond")
        return None
    else:
        # print(res)
        json = res.json()
        # print(json)
        if json.get('FAIL', None) == True:
            # print("* FAIL")
            return None
        elif json.get('LIST_SUCCEED', None) == True:
            # print("* Gotcha list!")
            return json.get('RESULT', None)
        else:
            # print("* Wrong token")
            return None


@mainPage.route('/', methods=['POST', 'GET'])
@mainPage.route('/index.html', methods=['POST', 'GET'])
@mainPage.route('/main', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        if not request.cookies.get('foo'):
            resp = make_response(render_template('index.html'))
            resp.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
        else:

            if not request.cookies.get('token'):
                resp = make_response(render_template('index.html', logged=False))
            else:
                user_login = request.cookies.get('login')
                user_token = request.cookies.get('token')

                result_list = try_get_jest_list(user_login, user_token)

                resp = make_response(render_template('index.html', logged=True, login=user_login, data=result_list))

        return resp
