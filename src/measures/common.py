'''
Created on Jul 30, 2014

@author: dbhage

Module containing functions common to measures
'''

def get_documents_per_author(author_articles):
    '''
    Get total number of articles for each author.
    @param author_articles: dict with article name as key and list of authors present in that article as value
    @return: dict with author as key and number of articles as value, None if author_articles is None or empty dict
    '''
    if not author_articles:
        return None
    
    docs_per_auth = dict()
    
    for article_name in author_articles.keys():
        for auth in author_articles[article_name]:
            if auth in docs_per_auth:
                docs_per_auth[auth] += 1
            else:
                docs_per_auth[auth] = 1

    return docs_per_auth