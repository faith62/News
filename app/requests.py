from concurrent.futures import process

import urllib.request, json
from .models import New


#Getting api key
api_key = None 

# Getting the movie base url
base_url = None 

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]

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

def search_new(new_name):
    search_new_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(api_key,new_name)
    with urllib.request.urlopen(search_new_url) as url:
        search_new_data = url.read()
        search_new_response = json.loads(search_new_data)

        search_new_article = None

        if search_new_response['article']:
            search_new_list = search_new_response['articles']
            search_new_article = process_articles(search_new_list)

    return search_new_article

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
        urlToImage = new_item.get('urlToImage')
        publishedAt = new_item.get('publishedAt')
        content = new_item.get('content')

        new_object = New(id ,author, title, description,url,urlToImage,publishedAt,content)
        new_articles.append(new_object)

    return new_articles

