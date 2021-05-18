from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, make_response
from ..config import jest_change_url, API_SECRET_KEY
import requests


jestEdit = Blueprint('jestEdit', __name__)


def try_change_jest(user_login, user_token, elem, value):
    params = dict(
        API_KEY = API_SECRET_KEY,
        QUERY = "ADD_JEST_LIST",

        LOGIN=user_login,
        TOKEN=user_token,
        ELEMENT=elem,
        VALUE=value
    )

    res = requests.post(jest_change_url, data=params)

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
        elif json.get('CHANGE_SUCCEED', None) == True:
            # print("* Changed successfully!")
            return json.get('RESULT', None)
        else:
            # print("* Wrong token")
            return None






@jestEdit.route('/jestEdit', methods=['POST', 'GET'])
def jest_edit():
    if request.method == 'GET':
        if not request.cookies.get('token'):
            return render_template('jest_edit.html')
        else:
            user_login = request.cookies.get('login')
            user_token = request.cookies.get('token')

            return render_template('jest_edit.html', login=user_login)

    elif request.method == 'POST':
        if not request.cookies.get('foo'):
            resp = make_response(render_template('jest_edit.html'), wrong=True)
            # resp.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
        else:
            user_login = request.cookies.get('login')
            user_token = request.cookies.get('token')

            number = int(request.form['number'])
            delta = int(request.form['delta'])


            result_list = try_change_jest(user_login, user_token, number, delta)
            if result_list is None:
                resp = make_response(render_template('jest_edit.html'), wrong=True)
            else:
                resp = make_response(redirect("/"))#,('index.html', login=user_login, data=result_list))

        return resp
