from flask import render_template, Blueprint

user = Blueprint('user_page', __name__, template_folder='templates', static_folder='static', url_prefix='/user', static_url_path='/static')


@user.route('/<name>')
def hello_user(name):
   if name =='admin':
      return render_template('admin.html')
      # http://127.0.0.1:5000/user/admin
   else:
      return render_template('user.html')
      # http://127.0.0.1:5000/user/x
      #  x = any name
