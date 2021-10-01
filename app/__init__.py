from flask import Flask
from config import Config

from .movies.routes import movies
from .authorization.routes import auth

from .models import db, login
from flask_migrate import Migrate


app = Flask(__name__)

app.register_blueprint(movies)
app.register_blueprint(auth)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

login.init_app(app)


from . import routes
from . import models

