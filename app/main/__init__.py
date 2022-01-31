from flask import Flask
from config import DevConfig
from flask import Bootstrap

app = Flask (__name__, innstance_relative_config = True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

boostrap = Bootstrap(app)
from app import views