from concurrent.futures import process
from app import app
import urllib.request, json
from .models import news

NEWS = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_news(id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_articles = None

        if get_news_response['articles']:
            new_articles_list =  get_news_response['articles']
            new_articles = process_articles(new_articles_list)

    return new_articles
