from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import submitHero
from flask_login import login_required

from app.models import db, Hero


movies = Blueprint('movies', __name__, template_folder='movies_templates')

@movies.route('/timeline')
def timeline():
    comic_universe='Marvel Studios'
    return render_template('timeline.html', universe=comic_universe)



@movies.route('/submithero', methods=['GET','POST'])
@login_required
def submit_hero():
    form = submitHero()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('form validated')
            newHero = Hero(hero=form.hero.data, movie=form.movie.data, movie_released=form.movie_released.data, actor=form.actor.data)
            try:
                db.session.add(newHero)
                db.session.commit()
            except:
                flash('Marvel Hero stated is already in the Database, please try again.', category='alert-danger')
                return redirect(url_for('movies.submit_hero'))


            flash('New Marvel Hero added!', category='alert-info')
            flash(f'{newHero.to_dict()}', category='alert-info')
            return redirect(url_for('movies.submit_hero'))
        else:
            flash('You entered incomplete or incorrect data, please try again', category='alert-danger')
            validated = False
        return redirect(url_for('movies.submit_hero'))
    return render_template('submitHero.html', form=form)
