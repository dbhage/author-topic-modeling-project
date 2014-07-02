'''
Created on Jul 1, 2014

@author: dbhage
'''

import unittest
from table.author_article import last_name_present
from author.author import Author

class TestAuthorArticleLNOP(unittest.TestCase):
    '''
    Test table.author_article.last_name_present
    '''

    def test_case1(self):
        '''
        TC1: Invalid case: author none.
        '''
        author = None
        article_content = "this is an article"
        actual = last_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed None as author")
        
    def test_case2(self):
        '''
        TC2: Invalid case: article none.
        '''
        author = Author()
        article_content = None
        actual = last_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed None as article_content")

    def test_case3(self):
        '''
        TC3: Invalid case: article=''.
        '''
        author = Author()
        article_content = ''
        actual = last_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed '' as article_content")

    def test_case4(self):
        '''
        TC4: Valid case: article has last names present
        '''
        author = Author()
        author.first_names = []
        author.last_names = ["Bhageerutty"]
        article_content = "This article talks about Bhageerutty"
        actual = last_name_present(author, article_content)
        self.assertTrue(actual, "function should return true, article contains last author's last name")

    def test_case5(self):
        '''
        TC5: Valid case: article does not have last name present but first name present
        '''
        author = Author()
        author.first_names = ["Bhageerutty"]
        author.last_names = ["Dwijesh"]
        article_content = "This article talks about Bhageerutty"
        actual = last_name_present(author, article_content)
        self.assertFalse(actual, "function should return false, article does not contain author's last name")
    
    def test_case6(self):
        '''
        TC6: Valid case: article has only one last name present
        '''
        author = Author()
        author.first_names = ["Dwijesh"]
        author.last_names = ["Bhageerutty", "Dean"]
        article_content = "This article talks about Bhageerutty"
        actual = last_name_present(author, article_content)
        self.assertFalse(actual, "function should return false, article does not contain all of author's last names")

    def test_case_7(self):
        '''
        TC7: Valid case: article has all last names present (2 last names)
        '''
        author = Author()
        author.first_names = ["Dwijesh"]
        author.last_names = ["Bhageerutty", "Dean"]
        article_content = "This article talks about Bhageerutty Dean, the writer from Mauritius."
        actual = last_name_present(author, article_content)
        self.assertTrue(actual, "function should return True, article contains all of author's last names")
