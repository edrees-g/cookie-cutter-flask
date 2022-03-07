from flask import Flask
from appname.extensions import bcrypt

from appname.controllers.root_controller import root_controller
from appname.controllers.favicon_controller import favicon_controller

from appname.controllers.home_controller import home_controller
from appname.controllers.about_controller import about_controller
from appname.controllers.signin_controller import signin_controller
from appname.controllers.signup_controller import signup_controller
from appname.controllers.signout_controller import signout_controller
from appname.controllers.contact_controller import contact_controller

from appname.controllers.dashboard.dashboard_controller import dashboard_controller
from appname.controllers.dashboard.example_controller import example_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object('appname.config.DevConfig')
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(root_controller)
    app.register_blueprint(favicon_controller)

    app.register_blueprint(home_controller)
    app.register_blueprint(about_controller)
    app.register_blueprint(signin_controller)
    app.register_blueprint(signup_controller)
    app.register_blueprint(signout_controller)
    app.register_blueprint(contact_controller)

    app.register_blueprint(dashboard_controller)
    app.register_blueprint(example_controller)
