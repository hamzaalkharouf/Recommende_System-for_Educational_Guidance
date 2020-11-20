from flask import render_template , Blueprint

home = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

@home.route('/')
def index():
    return render_template('index.html')
    # http://127.0.0.1:5000
@home.route('/static/Login')
def Login():
    return render_template('login.html')
    # http://127.0.0.1:5000/static/Login

@home.route('/static/Register')
def Register ():
    return render_template('Register.html')
    # http://127.0.0.1:5000/static/Register
