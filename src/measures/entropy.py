'''
Created on Jul 30, 2014

@author: dbhage

Module responsible for calculating entropy
'''

import math
from table.author_topic import AuthorTopic

def calculate_entropies(docs_per_auth, no_of_topics, author_topic_list, author_topic_counts, entropy_summation_func): 
    '''
    Calculate entropy values for all authors
    @param docs_per_auth: dict with author as key and number of articles as value
    @param no_of_topics: number of topics used
    @param author_topic_list: dict with author as key and list of topics associated as value
    @param author_topic_counts: 
    @return: dict with author as key and entropy value as value
    '''
    entropy_dict = dict()
    author_list = author_topic_list.keys()
    
    for auth in author_list:
        entropy = entropy_summation_func(auth, author_topic_list[auth], author_topic_counts, docs_per_auth[auth], formula_inside_sum)
        entropy *= -1/float(no_of_topics) #  multiply by -1/c
        entropy_dict[auth] = entropy
        
    return entropy_dict

def entropy_summation(auth, topic_list, author_topic_counts, n, formula_inside_sum_func):
    '''
    Evaluate summation part of formula
    @param auth: Author object
    @param topic_list: list of topics for auth
    @param author_topic_counts: dict with AuthorTopic objects as keys and counts as values
    @param n: total number of documents for that author
    @param formula_inside_sum_func: function to calculate the value inside of the summation
    @return: float representing the summation part of the entropy calculation if parameters valid, -1 otherwise
    '''
    if not auth or not topic_list or not author_topic_counts:
        raise ValueError("Entropy Summation getting invalid params")
    
    entropy_sum_only = 0
    for topic in topic_list:
        no_of_document_with_author_and_topic = author_topic_counts[AuthorTopic(auth, topic)]
        entropy_sum_only += formula_inside_sum_func(no_of_document_with_author_and_topic, n)
    return entropy_sum_only

def no_of_docs_with_topic(compositions):
    '''
    For all topics, find the number of documents containing the topic
    @param compositions: dict with document name as key and Composition object as value
    @return: dict with topic number as key and number of articles with that topic as value
    '''
    if not compositions:
        return None
    
    no_articles_with_topic = dict()
    
    for article_name in compositions.keys():
        topic = compositions[article_name].main_topic
        if topic in no_articles_with_topic:
            no_articles_with_topic[topic] += 1
        else:
            no_articles_with_topic[topic] = 1

    return no_articles_with_topic
    
def formula_inside_sum(nh, n):
    '''
    Formula inside the summation
    @param nh: number of documents with that topic, containing that author
    @param n: total number of documents for that author
    '''
    if nh < 0 or n <= 0:
        raise ValueError("Valid ranges: n > 0 and nh >= 0")
    if nh > n:
        raise ValueError("nh cannot be greater than n")
    return (nh/float(n)) * math.log(nh/float(n))