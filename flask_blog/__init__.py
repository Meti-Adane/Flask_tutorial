from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f38562b513d05c4a9e68ba32d2f7ca69'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manger = LoginManager(app)
login_manger.login_view = 'login'
login_manger.login_message_category='info'


from flask_blog import routes