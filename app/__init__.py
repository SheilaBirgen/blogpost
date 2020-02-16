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
login_manager.session_protection = 'strong'
app.config['SECRET_KEY'] ='05be4f8f478ca9ba4f40491dee332962'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')


# from app.people.routes import people
# from app.posts.routes import posts
# from app.main.routes import main



# app.register_blueprint(people)
# app.register_blueprint(posts)
# app.register_blueprint(main)
def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # configure UploadSet
    # configure_uploads(app,photos) #We then use the configure_uploads function and pass in the app instance and the UploadSet instance.

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app