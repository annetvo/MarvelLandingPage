from flask import Flask
from config import Config

from .movies.routes import movies

app = Flask(__name__)

app.register_blueprint(movies)

app.config.from_object(Config)

from . import routes

