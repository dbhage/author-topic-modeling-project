'''
Created on Jun 27, 2014

@author: dbhage
'''

import unittest
from author.author import Author
from table.author_article import find_authors
    
class TestAuthorArticleFindAuthor(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. No authors
        '''
        authors = []
        article_content = "This article contains no author"
        dictionary = dict()
        lnaofnp_func = always_false
        lnp_func = always_false
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)
        self.assertEquals(authors, [], "Invalid input should return []")

    def test_case2(self):
        '''
        TC2: Invalid case. authors=None
        '''
        authors = None
        article_content = "This article contains no author"
        dictionary = dict()
        lnaofnp_func = always_false
        lnp_func = always_false
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)
        self.assertEquals(authors, [], "Invalid input should return []")

    def test_case3(self):
        '''
        TC3: Invalid case. article_content = ''
        '''
        
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        authors = [author1]
        article_content = ""
        dictionary = dict()
        lnaofnp_func = always_false
        lnp_func = always_false
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)
        self.assertEquals(authors, [], "Invalid input should return []")

    def test_case4(self):
        '''
        TC4: Invalid case. article_content = None
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        authors = [author1]
        article_content = None
        dictionary = dict()
        lnaofnp_func = always_false
        lnp_func = always_false
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)
        self.assertEquals(authors, [], "Invalid input should return []")

    def test_case5(self):
        '''
        TC5: Invalid case. dictionary=None
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "no author present"
        dictionary = None
        lnaofnp_func = always_false
        lnp_func = always_false
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)
        self.assertEquals(authors, [], "Invalid input should return []")
    
    def test_case6(self):
        '''
        TC6: Valid case. last_name_in_dict = T, lnaofnp = T, lnp_func = T. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = {"neerav": "definition..."}

        lnaofnp_func = always_true
        lnp_func = always_true
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors[0], author1, "Match should be: " + str(author1))
    
    def test_case7(self):
        '''
        TC7: Valid case. last_name_in_dict = T, lnaofnp = T, lnp_func = F. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = {"neerav": "definition..."}

        lnaofnp_func = always_true
        lnp_func = always_false
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors[0], author1, "Match should be: " + str(author1))
        
    def test_case8(self):
        '''
        TC8: Valid case. last_name_in_dict = F, lnaofnp = T, lnp_func = T. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = dict()

        lnaofnp_func = always_true
        lnp_func = always_true
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors[0], author1, "Match should be: " + str(author1))

    def test_case9(self):
        '''
        TC9: Valid case. last_name_in_dict = F, lnaofnp = F, lnp_func = T. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = dict()

        lnaofnp_func = always_false
        lnp_func = always_true
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors[0], author1, "Match should be: " + str(author1))

    def test_case10(self):
        '''
        TC10: Valid case. last_name_in_dict = T, lnaofnp = F, lnp_func = T. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = {"neerav": "definition"}

        lnaofnp_func = always_false
        lnp_func = always_true
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors, [], "There should be no match.")

    def test_case11(self):
        '''
        TC11: Valid case. last_name_in_dict = T, lnaofnp = F, lnp_func = F. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = {"neerav": "definition"}

        lnaofnp_func = always_false
        lnp_func = always_false
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors, [], "There should be no match.")

    def test_case12(self):
        '''
        TC12: Valid case. last_name_in_dict = F, lnaofnp = T, lnp_func = F. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = dict()

        lnaofnp_func = always_true
        lnp_func = always_false
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors, [], "There should be no match.")

    def test_case13(self):
        '''
        TC13: Valid case. last_name_in_dict = F, lnaofnp = F, lnp_func = F. Match.
        '''
        author1 = Author()
        author1.first_names = ["dean"]
        author1.last_names = ["neerav"]
        
        authors = [author1]
        
        article_content = "article"
        dictionary = dict()

        lnaofnp_func = always_false
        lnp_func = always_false
        
        authors = find_authors(authors, article_content, dictionary, lnaofnp_func, lnp_func)

        self.assertEquals(authors, [], "There should be no match.")

def always_false(param1, param2):
    return False

def always_true(param1, param2):
    return True

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()