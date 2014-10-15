'''
Created on Oct 15, 2014

@author: dbhage

Detect languages in text using stop words.
'''

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from util.string import to_lower

def count_stopwords(text):
    '''
    Count stopwords in text

    @param text: text
    @type text: string

    @return: languages and their stopword counts found in the text
    @rtype: dict
    '''
    languages = {}

    tokens = wordpunct_tokenize(text)
    words = map(to_lower, tokens)

    for language in stopwords.fileids():

        stopwords_set = set(stopwords.words(language))
        
        count = 0
        for word in words:
            if word in stopwords_set:
                count += 1

        languages[language] = count
    
    return languages

def percentage_stopwords(languages):
    '''
    Get percentages+
    
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