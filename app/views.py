from email import message
from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message='news today'
    return render_template('index.html', message=message)

@app.route('/news/<id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = id)