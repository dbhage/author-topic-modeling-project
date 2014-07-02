'''
Created on Jul 1, 2014

@author: dbhage
'''

from util.io import get_lines
from composition import parse_compositions
import os
from author_article import find_authors, last_name_and_one_first_name_present, last_name_present

def get_compositions(compositions_file):
    lines = get_lines(compositions_file)
    compositions = parse_compositions(lines)
    return compositions

def get_author_articles(articles_folder, authors, dictionary, num=-1):
    file_names = sorted(os.listdir(articles_folder))

    if num < 0 or num >= len(file_names):
        num = len(file_names)
    
    author_articles = dict()
    
    for article in file_names[:num]:
        article_content = open(articles_folder + article).read()
        auths = find_authors(authors, article_content, dictionary, last_name_and_one_first_name_present, last_name_present)
        author_articles[article] = auths
    
    return author_articles

def author_topic_table(compositions_file, articles_folder, authors, dictionary):
    '''
    Produce an author-topic table based on compositions and author article data
    @param compositions:  dict with article name as key and composition object as value
    @param author_articles: dict with article name as key and author names list as value
    @return: list of AuthorTopic objects
    '''
    
    compositions = get_compositions(compositions_file)
    author_articles = get_author_articles(articles_folder, authors, dictionary, num=100)
    
    author_topics = []
    
    for article in compositions.keys():
        author_topics.append(AuthorTopic(author_articles[article], compositions[article].main_topic))
    
    return author_topics

class AuthorTopic(object):
    
    def __init__(self, names, topic):
        self.author = names
        self.topic = topic
    
    def __eq__(self, other):
        return self.author == other.author and self.topic == other.topic
    
    def __str__(self):
        return "Author:" + str(self.author) + " Topic: " + str(self.topic)