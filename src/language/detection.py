'''
Created on Oct 15, 2014

@author: dbhage

Detect languages in text using stop words.
'''

from nltk import wordpunct_tokenize
from util.string import to_lower

def count_stopwords(text, stopword_dict):
    '''
    Count stopwords in text

    @param text: text
    @type text: string

    @param stopword_dict: dict with lnaguage as key and stopword set as value
    @type stopword_dict: dict<str, set<str>>

    @return: languages and their stopword counts found in the text
    @rtype: dict
    '''
    languages = {}

    tokens = wordpunct_tokenize(text)
    words = map(to_lower, tokens)

    for (language, stopwords_set) in stopword_dict.items():

        count = 0
        for word in words:
            if word in stopwords_set:
                count += 1

        languages[language] = count
    
    return languages

def percentage_stopwords(languages):
    '''
    Get percentages
    
    @param languages: languages and counts
    @type languages: dict
    
    @return: languages and percentage
    @rtype: dict
    '''
    summation = float(sum(languages.values()))
    
    for d in languages.items():
        languages[d[0]] = d[1]/summation if summation != 0 else 0

    return languages

def detect_languages(text, count_stopwords_func, percentage_stopwords_func, threshold):
    '''
    Detect main languages in text
    
    @param text: text
    @type text: string

    @param count_stopwords_func: count stop words function
    @type count_stopwords_func: function
    
    @param percentage_stopwords_func: get percentage for stop word count function
    @type percentage_stopwords_func: function
    
    @param threshold: empirically determined number above which language presence is guaranteed
    @type threshold: float
    
    @return: list of languages 
    @rtype: list
    '''
    languages_dict = percentage_stopwords_func(count_stopwords_func(text))
    return [k for (k,v) in languages_dict.items() if v > threshold]

def stopword_proportion_per_language(stopword_dict, text):
    '''
    for each language, get the fraction of stopwords which are found in the text
    
    @param stopword_dict: dict with language as key and stop words as values
    @type stopword_dict: dict<str,set<str>>
    
    @param text: text
    @type text: str
    
    @return: dict with language as key and proportion as value
    @rtype: dict<str, float> 
    '''
    tokens = wordpunct_tokenize(text)
    words = map(to_lower, tokens)
    
    proportion_dict = {}
    
    for (language, stopword_list) in stopword_dict.items():
        
        found = set()
        
        for word in words:
            if word in stopword_list:
                found.add(word)
        
        proportion_dict[language] = float(len(found)) / len(stopword_list)

    return proportion_dict