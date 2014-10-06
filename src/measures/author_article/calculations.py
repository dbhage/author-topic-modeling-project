'''
Created on Oct 3, 2014

@author: dbhage

A. total number of articles
B. total number of articles with at least one author
C. total number of articles with at least two authors
D. % of articles with two different nationalities
E. % of articles with >=2 languages in the articles having >=2 authors
'''

from __future__ import division

class AuthorArticleCalculation(object):
    '''
    Author Article Calculation Class
    '''
    
    def __init__(self, author_articles, author_dict):
        '''
        Constructor
        @param author_articles: dict<article name, list of Author objects>
        @param author_dict: dict<author,language> 
        @postcondition: self.author_article_dict and self.language_article_dict are initialized and populated
        '''
        if not author_articles or not author_dict:
            raise ValueError("Input invalid.")

        self.author_article_dict = {}
        self.language_article_dict = {}

        for (article, authors) in author_articles.items():
            self.author_article_dict[article] = []
            self.language_article_dict[article] = []
            for author in authors:
                self.author_article_dict[article].append(str(author))
                self.language_article_dict[article].append(author_dict[str(author)])
    
    def get_no_of_articles(self):
        '''
        @return: number of articles
        '''
        return len(self.author_article_dict.keys())
    
    def get_no_of_articles_with_atleast_n_authors(self, n):
        '''
        Get the number of articles with at least n authors
        @param n: number of authors, n > 0
        @return: number of articles with n authors
        '''
        if n <= 0:
            raise ValueError("n must be > 0")
            
        count = 0
        for v in self.author_article_dict.values():
            if len(v) >= n:
                count += 1
        return count
    
    def get_percentage_articles_with_2_langs(self):
        '''
        Get the percentage of articles with 2 languages
        @return: percentage of articles with 2 languages
        '''
        if self.language_article_dict:
        
            count = 0
            
            for v in self.language_article_dict.values():
                if v:
                    for i in range(1, len(v)):
                        if v[i] != v[0]:
                            # new language
                            count += 1
                            break
            
            return count / len(self.language_article_dict)

        else:
            return 0

    def get_percentage_articles_with_2_langs_2_auths(self):
        '''
        Get the percentage of articles with >=2 languages in all articles with >=2 authors
        @return: float
        '''
        if self.language_article_dict:

            denominator = self.get_no_of_articles_with_atleast_n_authors(2)

            if denominator == 0:
                return 0

            count = 0
            
            for v in self.language_article_dict.values():
                if v:
                    if len(v) >= 2: # atleast 2 authors
                        for i in range(1, len(v)):
                            if v[i] != v[0]: # second lang found
                                count += 1
                                break
    
            return count / denominator
        
        else:
            return 0