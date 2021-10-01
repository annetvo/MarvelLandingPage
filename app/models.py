from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin
from datetime import datetime 
import uuid 

from werkzeug.security import generate_password_hash

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db = SQLAlchemy()

class Hero(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    hero = db.Column(db.String(150), nullable=False, unique=True)
    movie = db.Column(db.String(200))
    movie_released = db.Column(db.INTEGER)
    actor = db.Column(db.String(200))


    def to_dict(self):
        return {
            'id': self.id,
            'hero': self.hero,
            'movie': self.movie,
            'movie_released': self.movie_released,
            'actor':self.actor
        }


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, default='')  
    first_name = db.Column(db.String(200), nullable=True, default='')
    last_name = db.Column(db.String(200), nullable=True, default='') 
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid.uuid4())


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_created': self.date_created

        }