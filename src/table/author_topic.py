'''
Created on Jul 1, 2014

@author: dbhage
'''

def author_topic_table(compositions, author_articles):
    '''
    Produce an author-topic table based on compositions and author article data
    @param compositions: dict with article name as key and composition object as value
    @param author_articles: dict with article name as key and author names list as value
    @return: list of AuthorTopic objects
    '''
    if compositions is None or author_articles is None:
        return []
    
    author_topics = []
    
    for article in compositions.keys():
        for author in author_articles[article]:
            author_topic = AuthorTopic(author, compositions[article].main_topic)
            author_topics.append(author_topic)
    
    return author_topics

class AuthorTopic(object):
    def __init__(self, names, topic):
        self.author = names
        self.topic = topic
    
    def __eq__(self, other):
        return self.author == other.author and self.topic == other.topic
    
    def __str__(self):
        return "Author:" + str(self.author) + " Topic: " + str(self.topic)