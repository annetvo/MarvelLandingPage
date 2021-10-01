from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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