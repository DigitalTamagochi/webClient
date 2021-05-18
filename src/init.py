from flask import Flask
from .modules.login_group import loginApp
from .modules.register_group import registerApp
from .modules.server_main_page import mainPage
from .modules.jest_add_group import jestAdd
from .modules.jest_edit_group import jestEdit

app = Flask(__name__)

app.register_blueprint(loginApp)
app.register_blueprint(registerApp)
app.register_blueprint(mainPage)
app.register_blueprint(jestAdd)
app.register_blueprint(jestEdit)
