'''
Created on Jul 1, 2014

@author: dbhage
'''

import unittest
from table.author_article import last_name_and_one_first_name_present
from author.author import Author

class TestAuthorArticleLNAOFNP(unittest.TestCase):
    '''
    Test table.author_article.last_name_and_one_first_name_present
    '''
    def test_case1(self):
        '''
        TC1: Invalid case: author none.
        '''
        author = None
        article_content = "this is an article"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed None as author")
        
    def test_case2(self):
        '''
        TC2: Invalid case: article none.
        '''
        author = Author()
        article_content = None
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed None as article_content")

    def test_case3(self):
        '''
        TC3: Invalid case: article=''.
        '''
        author = Author()
        article_content = ''
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false on being passed '' as article_content")

    def test_case4(self):
        '''
        TC4: Valid case: last name and one first name present 
        '''
        author = Author()
        author.first_names = ["poi", "jul"]
        author.last_names = ["lois"]
        article_content = "poi j. lois was a great author"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertTrue(actual, "function should return True. Full last name and 1 first name present.")

    def test_case5(self):
        '''
        TC5: Valid case: last name present but no first name
        '''
        author = Author()
        author.first_names = ["poi", "jul"]
        author.last_names = ["lois"]
        article_content = "p.j. lois was a great author"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false. Full last name and atleast 1 first name NOT present.")

    def test_case6(self):
        '''
        TC6: Valid case: no last names and no first names present
        '''
        author = Author()
        author.first_names = ["poi", "jul"]
        author.last_names = ["lois"]
        article_content = "poi jul was a great author"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false. Full last name and atleast 1 first name NOT present.")

    def test_case7(self):
        '''
        TC7: Valid case: no last names but first name present
        '''
        author = Author()
        author.first_names = ["poi", "jul"]
        author.last_names = ["lois"]
        article_content = "poi was awesome as an author"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false. Full last name and atleast 1 first name NOT present.")

    def test_case8(self):
        '''
        TC8: Valid case: last name and all first name present
        '''
        author = Author()
        author.first_names = ["poi", "jul"]
        author.last_names = ["lois"]
        article_content = "poi jul lois was a great author"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertTrue(actual, "function should return True. Full last name and 1 first name present.")

    def test_case9(self):
        '''
        TC9: Valid case: part of last name and first name present
        '''
        author = Author()
        author.first_names = ["poi", "jul"]
        author.last_names = ["lois", "kundral"]
        article_content = "poi jul kundral was awesome as an author"
        actual = last_name_and_one_first_name_present(author, article_content)
        self.assertFalse(actual, "function should return false. Full last name and atleast 1 first name NOT present.")
