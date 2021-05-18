from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, make_response
from ..config import login_url, API_SECRET_KEY
import requests


loginApp = Blueprint('login', __name__)

# @loginApp.route('/logged_in', methods=['POST', 'GET'])
# def logged_in():
#     return render_template('logged_in.html')
#
# @loginApp.route('/logged_out', methods=['POST', 'GET'])
# def logged_out():
#     return render_template('logout.html')



@loginApp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':


        user_login = request.form['login']
        user_password = request.form['password']

        params = dict(
            API_KEY = API_SECRET_KEY,
            QUERY = "LOGIN",

            LOGIN=user_login,
            PASSWORD=user_password
        )

        res = requests.post(login_url, data=params)

        if res is None:
            return render_template('login.html', bad_request=True)
        else:
            # print(res)
            json = res.json()
            # print(json)
            if json.get('ACCESS_GRANTED', None) == True:
                # print("* Access granted")

                resp = make_response(redirect("/"))#, login=json.get('LOGIN', "fail"), login_success=True)
                resp.set_cookie("login", json.get('LOGIN', "fail"), max_age=60*60*24*15)
                resp.set_cookie("token", json.get('TOKEN', "fail"), max_age=60*60*24*15)
                # resp.headers['location'] = url_for('login.logged_in')
                return resp
                # return render_template('logged_in.html', login=user_login)

                # print("* Access granted")
                # return (user_login, json.get('TOKEN', None))
            else:
                return render_template('login.html', bad_login=True)
                # print("* Access denied")
                # return None



    elif request.method == 'GET':
        return render_template('login.html')


@loginApp.route('/logout', methods=['POST', 'GET'])
def logout():
    resp = make_response(render_template("logout.html"))
    resp.set_cookie('login', 'bar', max_age=0)
    resp.set_cookie('token', 'bar', max_age=0)
    # resp.headers['location'] = url_for('login.logged_out')
    return resp
