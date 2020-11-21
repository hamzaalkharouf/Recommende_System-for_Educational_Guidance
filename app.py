from flask import Flask
from home.views import home
from user_page.views import user
app = Flask(__name__, static_folder=None)


# to run =>  py app.py
if __name__ == '__main__':
    app.register_blueprint(home)
    app.register_blueprint(user)
    app.run(port=5000)
