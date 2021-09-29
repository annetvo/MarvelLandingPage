from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class submitHero(FlaskForm):
    hero = StringField('Superhero', validators=[DataRequired()])
    movie = StringField('Movie(s)')
    actor = StringField("Actor/Actresses's Name")
    submit_button = SubmitField('Submit')