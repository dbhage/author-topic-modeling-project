'''
Created on Oct 22, 2014

@author: dbhage
'''

import unittest

from table.author_article import get_last_name_count

class TestGetLastNameCount(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: invalid case, article_content None
        '''
        article_content = None
        last_name = "trottier"
        self.assertRaises(ValueError, get_last_name_count, article_content, last_name)

    def test_case2(self):
        '''
        TC2: invalid case, article_content empty
        '''
        article_content = ''
        last_name = "trottier"
        self.assertRaises(ValueError, get_last_name_count, article_content, last_name)
        
    def test_case3(self):
        '''
        TC3: invalid case, last_name None
        '''
        article_content = "yolo swaggins"
        last_name = None
        self.assertRaises(ValueError, get_last_name_count, article_content, last_name)

    def test_case4(self):
        '''
        TC4: invalid case, last_name empty
        '''
        article_content = "yolo swaggins"
        last_name = ''
        self.assertRaises(ValueError, get_last_name_count, article_content, last_name)
        
    def test_case5(self):
        '''
        TC5: valid case. last name not present
        '''
        article_content = "This is an article"
        last_name = "trottier"
        actual = get_last_name_count(article_content, last_name)
        expected = 0
        self.assertEqual(actual, expected)

    def test_case6(self):
        '''
        TC6: valid case. last name present once
        '''
        article_content = "This is an article about lorne trottier."
        last_name = "trottier"
        actual = get_last_name_count(article_content, last_name)
        expected = 1
        self.assertEqual(actual, expected)

    def test_case7(self):
        '''
        TC7: valid case. last name present twice
        '''
        article_content = "This is an article about lorne trottier. trottier donated a lot of money to our university"
        last_name = "trottier"
        actual = get_last_name_count(article_content, last_name)
        expected = 2
        self.assertEqual(actual, expected)

    def test_case8(self):
        '''
        TC8: valid case. last name present thrice
        '''
        article_content = "This is an article about lorne trottier. trottier donated a lot of money to our university. trottier?! botrottierbo"
        last_name = "trottier"
        actual = get_last_name_count(article_content, last_name)
        expected = 3
        self.assertEqual(actual, expected)

    def test_case9(self):
        '''
        TC9
        '''
        article_content = "ching li\nchun li\n"
        last_name = "li"
        actual = get_last_name_count(article_content, last_name)
        expected = 2
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()