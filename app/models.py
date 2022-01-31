class Sources:
    """
    news class to define News objects
    """

    def __init__(self,id,name,author,title,description,publishedAt,Image,url):
        self.id =id
        self.name =name
        self.author = author
        self.title = title
        self.description =description
        self.publishedAt =publishedAt
        self.Image = Image
        self.url = url



class Articles:
    """
    article class defining article objects
    """

    def __init__(self,name,author,title,description,publishedAt,urlToImage,url):
      
        self.name =name
        self.author = author
        self.title = title
        self.description =description
        self.publishedAt =publishedAt
        self.urlToImage =urlToImage
        self.url =url        