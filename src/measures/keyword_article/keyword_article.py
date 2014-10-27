'''
Created on Oct 27, 2014

@author: dbhage

Data structure to store sums of keyword occurrences and tokens from articles, subset by year, for all articles
'''

from __future__ import division

class KeywordArticle(object):
    '''
    @summary: Data structure to store sums of keywords and token subset by year for all articles
    '''

    def __init__(self, keywords, year):
        '''
        Constructor
        
        @param keywords: list of keywords
        @type keywords: str list
        
        @param year: year for KeywordArticle
        @type year: int
        
        @postcondition: self.keywords_dict initialized with keywords as keys and 0 as values
        @postcondition: self.tokens initialized with empty set 
        @postcondition: self.year, self.keywords created
        @postcondition: self.no_of_articles set to 0
        '''
        self.keywords_dict = {k:0 for k in keywords}
        self.tokens = set()
        self.year = year
        self.no_of_articles = 0
        self.keywords = keywords
        
    def normalize(self):
        '''
        Normalize values using number of tokens
        
        @postcondition: tokens set None
        @postcondition: keyword sums normalized
        '''
        no_of_tokens = len(self.tokens)
        for keyword in self.keywords:
            self.keywords_dict[keyword] /= no_of_tokens
        self.tokens = None
        
    def add_to_keyword(self, keyword, count):
        '''
        Add count to keyword's current sum
        
        @param keyword: the keyword
        @type keyword: str
        
        @param count: the number to be added
        @type count: int
        
        @postcondition: keyword's sum incremented by count
        '''
        self.keywords_dict[keyword] += count
    
    def add_to_tokens(self, new_tokens):
        '''
        Add tokens to current token set
        
        @param new_tokens: list of tokens
        @type new_tokens: str list
        
        @postcondition: self.tokens now contains the new tokens in new_tokens
        '''
        self.tokens |= set(new_tokens)
    
    def __getitem__(self, keyword):
        '''
        Overload [] operator
        
        @param keyword: keyword
        @type keyword: str
        
        @return: current sum value for that keyword
        @rtype: float
        '''
        return float(self.keywords_dict[keyword])
    
    def __str__(self, *args, **kwargs):
        '''
        Overload str()
        
        @return: string representation of this KeywordArticle obj
        @rtype: str
        '''
        s = str(self.year) + ','
        
        for i,keyword in enumerate(self.keywords):
            s += str(self.keywords_dict[keyword])
            if i < len(self.keywords) - 1:
                # not last
                s += ','
            else:
                s += '\n'
                
        return s