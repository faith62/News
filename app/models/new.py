class New:
    '''
    News class to define news Objects
    '''

    def __init__(self,id ,author, title, description,url,urlToimage,publishedAt,content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToimage = urlToimage
        self.publishedAt = publishedAt
        self.content = content
