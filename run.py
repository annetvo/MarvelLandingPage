
from app import app
from app.models import db, User, Hero
from app.api.routes import heroes

@app.shell_context_processor
def shell_context():
    return {'db':db, 'User':User, 'Hero':Hero, 'HeroRoute':heroes}