'''
Created on Jul 29, 2014

@author: dbhage
'''
from common import get_documents_per_author

def calculate_purities(author_articles, most_dominant):
    '''
    @return: dict with author as key and purity as value
    '''
    docs_per_auth = get_documents_per_author(author_articles)
    
    purity_dict = dict()
    
    for (auth, no_articles_for_author) in docs_per_auth.items():
        print (auth)

        dominant_topic = most_dominant[auth][0]
        print ("Dominant Topic: " + str(dominant_topic))

        no_articles_with_dominant_topic = most_dominant[auth][1]

        print ("#Articles with dominant topic: " + str(no_articles_with_dominant_topic))
        print ("#Articles for Author: " + str(no_articles_for_author))
        
        purity = calculate_purity(no_articles_for_author, no_articles_with_dominant_topic)
        print ("Purity: " + str(purity))
        print ("---------------")
    
        purity_dict[auth] = purity
    
    return purity_dict

def calculate_purity(n, h):
    '''
    Calculate purity for ONE author.
    @param n: total number of articles for that author
    @param h: number of articles that contain most dominant topic for an author
    @return: float representing the purity value
    '''
    return (1/float(n))*h if (n>0 and h>=0) else -1