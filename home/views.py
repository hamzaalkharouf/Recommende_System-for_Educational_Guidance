from flask import render_template , Blueprint

home = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

@home.route('/')
def landing():
    return render_template('landing.html')
    # http://127.0.0.1:5000

# @home.route('/static/landing')
# def landing():
#     return render_template('landing.html')
#     # http://127.0.0.1:5000/static/landing
@home.route('/static/result')
def result():
    return render_template('result.html')
    # http://127.0.0.1:5000/static/result

@home.route('/static/signup')
def signup():
    return render_template('signup_e.html')
    # http://127.0.0.1:5000/static/signup

@home.route('/static/Login')
def Login():
    return render_template('login_e.html')
    # http://127.0.0.1:5000/static/Login
