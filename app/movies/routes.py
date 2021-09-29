from flask import Blueprint, render_template, request
from app.forms import submitHero


movies = Blueprint('movies', __name__, template_folder='movies_templates')

@movies.route('/timeline')
def timeline():
    comic_universe='Marvel Studios'
    return render_template('timeline.html', universe=comic_universe)


@movies.route('/submithero', methods=['GET','POST'])
def submit_hero():
    form = submitHero()
    if request.method == 'POST':
        if form.validate_on_submit(): 
            print('form validated')
        else:
            print('form did not validate')
    return render_template('submitHero.html', form=form)
