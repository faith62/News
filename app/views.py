
from flask import render_template
from app import app
from app.request import get_news

# Views
@app.route('/')
def new():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Find the latest news'

    bbc_news = get_news('bbc-news')
    print(bbc_news)
    return render_template('index.html', title = title, bbc = bbc_news)

# @app.route('/news/<id>')
# def new(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     title = f'You are viewing {id}'
#     return render_template('news.html',title = title)