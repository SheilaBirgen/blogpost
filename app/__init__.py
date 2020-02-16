import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

app.config['SECRET_KEY'] ='05be4f8f478ca9ba4f40491dee332962'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from app.people.routes import people
from app.posts.routes import posts
from app.main.routes import main



app.register_blueprint(people)
app.register_blueprint(posts)
app.register_blueprint(main)
