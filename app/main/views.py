
from flask import render_template,request,redirect,url_for
from app import app
from app.request import get_news, search_new


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Find the latest news'

    bbc_news = get_news('bbc-news')
    cnn_news = get_news('cnn')
    business_news = get_news('business-insider')
    # print(bbc_news)

    search_new = request.args.get('new_query')

    if search_new:
        return redirect(url_for('search',new_name = search_new))
    else:       
        return render_template('index.html', title = title, bbc = bbc_news,cnn = cnn_news,business =business_news)

@app.route('/search/<new_name>')
def new(new_name):

    '''
    View function to display the search results
    '''
    new_name_list = new_name.split(" ")
    new_name_format = "+".join(new_name_list)
    searched_news = search_new(new_name_format)
    title = f'search results for {new_name}'
    return render_template('search.html',news = searched_news)