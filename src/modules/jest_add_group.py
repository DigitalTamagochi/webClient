from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, make_response
from ..config import jest_add_url, API_SECRET_KEY
import requests


jestAdd = Blueprint('jestAdd', __name__)


def try_add_jest(user_login, user_token, elem):
    params = dict(
        API_KEY = API_SECRET_KEY,
        QUERY = "ADD_JEST_LIST",

        LOGIN=user_login,
        TOKEN=user_token,
        ELEMENT=elem
    )

    res = requests.post(jest_add_url, data=params)

    if res is None:
        # print("> Something gone wrong, server does not respond")
        return None
    else:
        print(res)
        json = res.json()
        # print(json)
        if json.get('FAIL', None) == True:
            # print("* FAIL")
            return None
        elif json.get('ADD_SUCCEED', None) == True:
            # print("* Added to list!")
            return json.get('RESULT', None)
        else:
            # print("* Wrong token")
            return None




@jestAdd.route('/jestAdd', methods=['POST', 'GET'])
def jest_add():
    if request.method == 'GET':
        if not request.cookies.get('token'):
            return render_template('jest_add.html')
        else:
            user_login = request.cookies.get('login')
            user_token = request.cookies.get('token')

            return render_template('jest_add.html', login=user_login)

    elif request.method == 'POST':
        if not request.cookies.get('foo'):
            resp = make_response(render_template('jest_add.html'))
            # resp.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
        else:
            user_login = request.cookies.get('login')
            user_token = request.cookies.get('token')

            number = int(request.form['number'])

            result_list = try_add_jest(user_login, user_token, number)
            if result_list is None:
                resp = make_response(render_template('jest_add.html'))
            else:
                resp = make_response(redirect("/"))#,('index.html', login=user_login, data=result_list))

        return resp
