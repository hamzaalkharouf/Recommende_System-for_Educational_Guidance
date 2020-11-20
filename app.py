from flask import Flask
from home.views import home
from user_page.views import user
app = Flask(__name__, static_folder=None)

app.register_blueprint(home)
app.register_blueprint(user)

# to run =>  flask run 
