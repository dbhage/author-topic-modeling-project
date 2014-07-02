'''
Created on Jul 1, 2014

@author: dbhage
'''

import unittest
from table.author_article import full_name_present
from author.author import Author

class TestAuthorArticleFNP(unittest.TestCase):
    '''
    Test table.author_article.full_name_present
    '''
    def test_case1(self):
        '''
        TC1: Invalid case: author none.
        '''
        author = None
        article_content = "this is an article"
        actual = full_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed None as author")
        
    def test_case2(self):
        '''
        TC2: Invalid case: article none.
        '''
        author = Author()
        article_content = None
        actual = full_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed None as article_content")

    def test_case3(self):
        '''
        TC3: Invalid case: article=''.
        '''
        author = Author()
        article_content = ''
        actual = full_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed '' as article_content")
    
    def test_case4(self):
        '''
        TC4: valid case: full name present with author having 1 first name and 1 last name
        '''
        author = Author()
        author.first_names = ["Dean"]
        author.last_names = ["Neerav"]
        article_content = "Dean Neerav was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertTrue(actual, "function should return True, full name present")
    
    def test_case5(self):
        '''
        TC5: valid case: full name present with author having 1 first name and multiple last names
        '''
        author = Author()
        author.first_names = ["Dean"]
        author.last_names = ["Neerav", "Boundo"]
        article_content = "Dean Neerav Boundo was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertTrue(actual, "function should return True, full name present")
    
    def test_case6(self):
        '''
        TC6: valid case: full name present with author having multiple first names and 1 last name
        '''
        author = Author()
        author.first_names = ["Dean", "Illahi"]
        author.last_names = ["Neerav"]
        article_content = "Dean Illahi Neerav was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertTrue(actual, "function should return True, full name present")
    
    def test_case7(self):
        '''
        TC7: valid case: full name present with author having multiple first names and multiple last names
        '''
        author = Author()
        author.first_names = ["Dean", "Illahi"]
        author.last_names = ["Neerav", "Boundo"]
        article_content = "Dean Illahi Neerav Boundo was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertTrue(actual, "function should return True, full name present")

    def test_case8(self):
        '''
        TC8: valid case: full name not present, first name present but not last name
        '''
        author = Author()
        author.first_names = ["Dean"]
        author.last_names = ["Neerav"]
        article_content = "Dean was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertFalse(actual, "function should return false, full name not present")

    def test_case9(self):
        '''
        TC9: valid case: full name not present, last name present but not first name
        '''
        author = Author()
        author.first_names = ["Dean", "Boundo"]
        author.last_names = ["Neerav"]
        article_content = "Neerav was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertFalse(actual, "function should return false, full name not present")

    def test_case10(self):
        '''
        TC10: valid case: full name not present, none of last or first name present
        '''
        author = Author()
        author.first_names = ["Dean", "Boundo"]
        author.last_names = ["Neerav"]
        article_content = "Bibu was a particularly murderous author. Even GRRM would come second to him when it came to murdering main characters."
        actual = full_name_present(author, article_content)
        self.assertFalse(actual, "function should return false, full name not present")
