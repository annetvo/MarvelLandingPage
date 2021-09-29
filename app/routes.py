from app import app
from flask import render_template

@app.route('/')
def home():
    comic_universe='Marvel Studios'
    return render_template('index.html', universe=comic_universe)


