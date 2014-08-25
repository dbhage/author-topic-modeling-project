'''
Created on Aug 25, 2014

@author: dbhage
'''

def get_co_occurrence_list(co_occurrence_dict):
    '''
    @param co_occurrence_dict: dict with CoOccurrence object as key and weight as value
    @return: list of 3-tuples in this format: (auth1, auth2, weight), where weight = #times auth1 and auth2 co-occur
             in unique articles.
    '''
    return [(str(k.author1), str(k.author2), v) for (k,v) in co_occurrence_dict.items()]

def get_co_occurrence_dict(author_articles, list_all_co_occurences_func):
    '''
    Get co-occurrence with weight
    @param author_articles: dict with article name as key and list of authors present in that article as value
    @param list_all_co_occurences_func: function to list all occurrences which takes a list of authors as input
    @return: dict with CoOccurrence object as key and weight as value
    '''
    if not author_articles:
        return None
        
    co_occurrence_dict = dict()

    for author_list in author_articles.values():
        co_occurences = list_all_co_occurences_func(author_list)
    
        if co_occurences:
            for co_occurrence in co_occurences:
                if co_occurrence in co_occurrence_dict:
                    co_occurrence_dict[co_occurrence] += 1
                else:
                    co_occurrence_dict[co_occurrence] = 1
    
    return co_occurrence_dict

def list_all_co_occurences(author_list):
    '''
    Find list of all co-occurrences for all authors in article
    @param author_list: list of authors
    @return: list of CoOccurence objects
    '''
    if not author_list:
        return None
    
    co_occurrences = []
    
    for i in range(0, len(author_list)):
        for j in range(i+1, len(author_list)):
            co_occurrences.append(CoOccurrence(author_list[i], author_list[j]))

    return co_occurrences

class CoOccurrence(object):

    def __init__(self, auth1, auth2):
        self.author1 = auth1
        self.author2 = auth2
    
    def __eq__(self, other):
        return self.author1 == other.author1 and self.author2 == other.author2
    
    def __hash__(self):
        return hash((self.author1, self.author2))
