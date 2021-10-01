from flask import Flask
from config import Config

from .movies.routes import movies

from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.register_blueprint(movies)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)



from . import routes
from . import models

