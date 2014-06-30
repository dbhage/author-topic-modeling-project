'''
Created on Jun 27, 2014

@author: dbhage
'''

import unittest

from author.author import Author

from parser.author_article import last_name_present
from parser.author_article import last_name_and_one_first_name_present
from parser.author_article import full_name_present

from parser.author_article import find_authors

class TestAuthorArticleLNOP(unittest.TestCase):
    '''
    Test parser.author_article.last_name_present
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

class TestAuthorArticleLNAOFNP(unittest.TestCase):
    '''
    Test parser.author_article.last_name_and_one_first_name_present
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

class TestAuthorArticleFNP(unittest.TestCase):
    '''
    Test parser.author_article.full_name_present
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
    
class TestAuthorArticleFindAuthor(unittest.TestCase):
    # TODO
    def test_case1(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()