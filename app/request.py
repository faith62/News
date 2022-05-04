from concurrent.futures import process
from app import app
import urllib.request, json
from .models import new

New = new.New

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

def process_articles(new_list):
    '''
    Function  that processes the new result and transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns :
        new_articles: A list of new objects
    '''
    new_articles = []
    for new_item in new_list:
        id = new_item.get('id')
        author = new_item.get('author')
        title = new_item.get('title')
        description = new_item.get('description')
        url = new_item.get('url')
        urlToimage = new_item.get('urlToimage')
        publishedAt = new_item.get('publishedAt')
        content = new_item.get('content')

        new_object = New(id ,author, title, description,url,urlToimage,publishedAt,content)
        new_articles.append(new_object)

    return new_articles

