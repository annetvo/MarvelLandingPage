from flask import Blueprint, render_template


movies = Blueprint('movies', __name__, template_folder='movies_templates')

@movies.route('/history')
def history():
    comic_universe='Marvel Studios'
    return render_template('history.html', universe=comic_universe)
