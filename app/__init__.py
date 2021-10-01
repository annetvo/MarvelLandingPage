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
login.login_view = 'auth.signin'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'alert-info'


from . import routes
from . import models

