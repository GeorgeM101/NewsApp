from ..request import get_articles, get_sources
from flask import render_template
from . import main

@main.route('/')
def index():
    
    general_sources = get_sources('general')
    business_news = get_sources('business')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    science_sources = get_sources('science')
    health_sources = get_sources('health')
    sports_sources = get_sources('sports')
    
    title = 'InterNews Bringing the world to you.'
    return render_template('index.html', title = title,general = general_sources,business=business_news,technology =technology_sources,enternainment= entertainment_sources,sports =sports_sources,science = science_sources,health= health_sources)

@main.route('/source/<source_id>')
def artcicles(source_id):

    '''
    View news page function that returns the news details page and its data
    '''
    
    return render_template('index.html',id = source_id)

@main.route('/source/<int:id>')
def source(id):

    '''
    View source page function that returns the movie details page and its data
    '''
    source = get_sources(id)
    title = f'{source.title}'

    return render_template('news.html',title = title,source= source)    


@main.route('/articles/<id>')
def article(id):

    '''
    View news page function that returns the news details page and its data
    '''
    article = get_articles(id)
    title = f'{id}'

    return render_template('news.html',title = title,article= article)        
