from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, make_response
from ..config import register_url, API_SECRET_KEY
import requests


registerApp = Blueprint('register', __name__)

@registerApp.route('/register', methods=['POST', 'GET'])
def register_app():
    if request.method == 'POST':


        user_login = request.form['login']
        user_password = request.form['password']
        user_password2 = request.form['password2']
        user_email = "lol@lol.ru",#request.form['email']
        user_first_name = "lol",# request.form['first_name']
        user_second_name = "lol"#request.form['second_name']

        if user_password != user_password2:
            return render_template('register.html', not_equal_passwords=True)

        params = dict(
            API_KEY = API_SECRET_KEY,
            QUERY = "REGISTRATION",

            LOGIN = user_login,
            PASSWORD = user_password,
            EMAIL =  user_email,
            FIRST_NAME = user_first_name,
            SECOND_NAME = user_second_name
        )


        res = requests.post(register_url, data=params)
        print("SEND REGI")
        if res is None:
            return render_template('register.html', bad_request=True)
        else:
            # print(res)
            json = res.json()
            # print(json)
            if json.get('REGISTRATION_SUCCEED', False) == True:
                resp = make_response(redirect("/"))#, login=json.get('LOGIN', "fail"), login_success=True)
                resp.set_cookie("login", user_login, max_age=60*60*24*15)
                resp.set_cookie("token", json.get('TOKEN', "fail"), max_age=60*60*24*15)
                # resp.headers['location'] = url_for('login.logged_in')
                return resp
                # return render_template('logged_in.html', login=user_login)

                # print("* Access granted")
                # return (user_login, json.get('TOKEN', None))
            else:
                return render_template('register.html', bad_login=True)
                print("* Access denied")
                # return None



    elif request.method == 'GET':
        return render_template('register.html')
