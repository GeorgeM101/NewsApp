
# from app.models import articles
import os

class Config:
    """
    General configaration parent class
    """
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    
    EVERYTHING_SOURCE_API_URL= 'https://newsapi.org/v2/everything?q={}&apiKey={}'

    SOURCE_API_KEY = os.environ.get('SOURCE_API_KEY')

    
class ProdConfig(Config):
    """
     Class that configures production
    """

    pass


class DevConfig(Config):

    DEBUG =True  

config_options = {
'development':DevConfig,
'production':ProdConfig
}    