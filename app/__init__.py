from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.session_protection = 'strong'


def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Creating the app configuration
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

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    
    # configure UploadSet
    configure_uploads(app,photos)

    return app