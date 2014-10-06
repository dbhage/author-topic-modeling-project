'''
Created on Oct 5, 2014

@author: dbhage

Module to test measures.author_article.calculations.AuthorArticleCalculation class.
'''

import unittest
from measures.author_article.calculations import AuthorArticleCalculation

class TestGetNoOfArticles(unittest.TestCase):
    '''
    Class to test measures.author_article.calculations.AuthorArticleCalculation.get_no_of_articles()
    '''
    def test_case1(self):
        '''
        TC1: 0 articles
        '''
        author_article_dict = {}
        language_article_dict = {}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_no_of_articles()
        expected = 0
        self.assertEqual(actual, expected)

    def test_case2(self):
        '''
        TC2: 1 article
        '''
        author_article_dict = {"article1":[]}
        language_article_dict = {"article1":[]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_no_of_articles()
        expected = 1
        self.assertEqual(actual, expected)

    def test_case3(self):
        '''
        TC3: 2 articles
        '''
        author_article_dict = {"article1":[], "article2":[]}
        language_article_dict = {"article1":[], "article2":[]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_no_of_articles()
        expected = 2
        self.assertEqual(actual, expected)

class TestGetNoOfArticlesWithAtLeastNAuthors(unittest.TestCase):
    '''
    Class to test measures.author_article.calculations.AuthorArticleCalculation.get_no_of_articles_with_atleast_n_authors(n) class.
    '''
    
    def test_case_1(self):
        '''
        TC1: Invalid Case. n=-1
        '''
        author_article_dict = {}
        language_article_dict = {}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = -1
        self.assertRaises(ValueError, aac.get_no_of_articles_with_atleast_n_authors, n)

    def test_case_2(self):
        '''
        TC2: Invalid, Boundary Case. n=0
        '''
        author_article_dict = {}
        language_article_dict = {}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 0
        self.assertRaises(ValueError, aac.get_no_of_articles_with_atleast_n_authors, n)

    def test_case_3(self):
        '''
        TC3: Valid, Boundary Case. n=1, there are no articles with at least 1 author
        '''
        author_article_dict = {}
        language_article_dict = {}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 1
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 0
        self.assertEqual(actual, expected)

    def test_case_4(self):
        '''
        TC4: Valid, Boundary Case. n=1, there is 1 article with at least 1 author
        '''
        author_article_dict = {"article1":["author1"]}
        language_article_dict = {"article1":["language1"]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 1
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_case_5(self):
        '''
        TC5: Valid, Boundary Case. n=1, dict has 1 article with 1 author
        '''
        author_article_dict = {"article1":["author1"]}
        language_article_dict = {"article1":["language1"]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 1
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 1
        self.assertEqual(actual, expected)

    def test_case_6(self):
        '''
        TC6: Valid, Boundary Case. n=1, dict has 2 articles, 1 with an author, 1 with 0 authors
        '''
        author_article_dict = {"article1":["author1"], "article2":[]}
        language_article_dict = {"article1":["language1"], "article2":[]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 1
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 1
        self.assertEqual(actual, expected)

    def test_case_7(self):
        '''
        TC7: Valid Case. n=2, no article has >=2 authors
        '''
        author_article_dict = {"article1":["author1"], "article2":["author1"]}
        language_article_dict = {"article1":["language1"], "article2":["language1"]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 2
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 0
        self.assertEqual(actual, expected)

    def test_case_8(self):
        '''
        TC8: Valid Case. n=2, 1 article has >=2 authors
        '''
        author_article_dict = {"article1":["author1", "author2"], "article2":["author1"]}
        language_article_dict = {"article1":["language1", "language2"], "article2":["language1"]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 2
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_case_9(self):
        '''
        TC9: Valid Case. n=2, 2 articles have >=2 authors
        '''
        author_article_dict = {"article1":["author1", "author2"], 
                               "article2":["author1", "author2"],
                               "article3":[]}
        
        language_article_dict = {"article1":["language1", "language2"], 
                                 "article2":["language1", "language2"],
                                 "article3":[]}

        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        n = 2
        actual = aac.get_no_of_articles_with_atleast_n_authors(n)
        expected = 2
        self.assertEqual(actual, expected)

class TestGetPercentageOfArticlesWith2Languages(unittest.TestCase):
    '''
    Class to test measures.author_article.calculations.AuthorArticleCalculation.get_percentage_articles_with_2_langs() method.
    '''

    def test_case_1(self):
        '''
        TC1: no article with 2 languages - empty dict
        '''
        author_article_dict = {}
        language_article_dict = {}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs()
        expected = 0
        self.assertEqual(actual, expected)

    def test_case_2(self):
        '''
        TC2: no article with 2 languages - dict has articles with 0 or 1 language only
        '''
        author_article_dict = {}
        language_article_dict = {"article1":[], "article2":["language1", "language1", "language1"]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs()
        expected = 0
        self.assertEqual(actual, expected)

    def test_case_3(self):
        '''
        TC3: 1 article with 2 languages
        '''
        author_article_dict = {}
        language_article_dict = {"article1":["language3"], "article2":["language1", "language1", "language2"]}
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs()
        expected = .5
        self.assertAlmostEqual(actual, expected, 3)

    def test_case_4(self):
        '''
        TC4: 2 articles with 2 languages
        '''
        author_article_dict = {}
        
        language_article_dict = {"article1":["language3"], 
                                 "article2":["language1", "language1", "language2"],
                                 "article3":["language4", "language6", "language4"]}
        
        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs()
        expected = .667
        self.assertAlmostEqual(actual, expected, 3)

class TestGetPercentageOfArticlesWith2Languages2Authors(unittest.TestCase):
    '''
    Class to test measures.author_article.calculations.AuthorArticleCalculation.get_percentage_articles_with_2_langs_2_auths() method.
    '''

    def test_case1(self):
        '''
        TC1: no articles have 2 authors or 2 languages
        '''
        
        author_article_dict = {"article1":["author1"], 
                               "article2":["author1"],
                               "article3":[]}
        
        language_article_dict = {"article1":["language1"], 
                                 "article2":["language1"],
                                 "article3":[]}

        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs_2_auths()
        expected = 0
        self.assertEqual(actual, expected)

    def test_case2(self):
        '''
        TC2: There are articles with 2 authors but not 2 languages
        '''
        author_article_dict = {"article1":["author1", "author2"], 
                               "article2":["author1", "author2"],
                               "article3":[]}
        
        language_article_dict = {"article1":["language1", "language1"], 
                                 "article2":["language1", "language1"],
                                 "article3":[]}

        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs_2_auths()
        expected = 0
        self.assertEqual(actual, expected)

    def test_case3(self):
        '''
        TC3: 1 article has 2 authors and 2 languages
        '''
        author_article_dict = {"article1":["author1", "author2"], 
                               "article2":["author1", "author3"],
                               "article3":[]}
        
        language_article_dict = {"article1":["language1", "language2"], 
                                 "article2":["language1", "language1"],
                                 "article3":[]}

        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs_2_auths()
        expected = .5
        self.assertAlmostEqual(actual, expected, 1)

    def test_case4(self):
        '''
        TC4: 2 articles have 2 authors and 2 languages
        '''
        author_article_dict = {"article1":["author1", "author2"], 
                               "article2":["author4", "author3"],
                               "article3":[]}
        
        language_article_dict = {"article1":["language1", "language2"], 
                                 "article2":["language4", "language3"],
                                 "article3":[]}

        aac = AuthorArticleCalculation1(author_article_dict, language_article_dict)
        actual = aac.get_percentage_articles_with_2_langs_2_auths()
        expected = 1
        self.assertEqual(actual, expected)

class AuthorArticleCalculation1(AuthorArticleCalculation):
    '''
    Override the constructor so we can test the methods independently.
    '''
    def __init__(self, author_article_dict, language_article_dict):
        '''
        Override constructor
        @param author_article_dict: dict<article,author list as a list of strings>
        @param language_article_dict: dict<article,language list as a list of strings>
        '''
        self.author_article_dict = author_article_dict
        self.language_article_dict = language_article_dict

if __name__ == "__main__":
    unittest.main()