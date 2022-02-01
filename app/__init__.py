from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_name):

#init the application
    app = Flask(__name__,instance_relative_config= True)

#setting up configuration
    app.config.from_object(config_options[config_name])
# app.config.from_pyfile('config.py')

#initialzing Flask Extention
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # setting config
    from .request import configure_request
    configure_request(app)


    return app


