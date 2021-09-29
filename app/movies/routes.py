from flask import Blueprint, render_template


movies = Blueprint('movies', __name__, template_folder='movies_templates')

@movies.route('/timeline')
def timeline():
    comic_universe='Marvel Studios'
    return render_template('timeline.html', universe=comic_universe)
