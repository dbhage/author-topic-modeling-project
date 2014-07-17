'''
Created on Jul 17, 2014

@author: dbhage

Test measures.author_name_recognition.ArticleAuthorContent's Constructor
'''

import unittest

from measures.author_name_recognition import ArticleAuthorContent

class TestArticleAuthorContentConstructor(unittest.TestCase):
    '''
    Test measures.author_name_recognition.ArticleAuthorContent's Constructor
    '''
    def test_case1(self):
        '''
        TC1: Invalid Case: Input none
        '''
        article_id = None
        self.assertRaises(ValueError, ArticleAuthorContent, article_id)
    
    def test_case2(self):
        '''
        TC2: Invalid Case: Input negative number
        '''
        article_id = -11
        self.assertRaises(ValueError, ArticleAuthorContent, article_id)
    
    def test_case3(self):
        '''
        TC3: Invalid Boundary Case: Input 0
        '''
        article_id = 0
        self.assertRaises(ValueError, ArticleAuthorContent, article_id)

    def test_case4(self):
        '''
        TC4: Valid Boundary Case: Input 1
        '''
        article_id = 1
        article_author_content = ArticleAuthorContent(article_id)

        self.assertDictEqual(article_author_content.mentions, dict(), "Dicts do not match")
        self.assertEqual(article_author_content.article_id, article_id, 
                         "Expected: " + str(article_id) + "Found: " + str(article_author_content.article_id))

    def test_case5(self):
        '''
        TC5: Valid Case: Input 223
        '''
        article_id = 223
        article_author_content = ArticleAuthorContent(article_id)

        self.assertDictEqual(article_author_content.mentions, dict(), "Dicts do not match")
        self.assertEqual(article_author_content.article_id, article_id, 
                         "Expected: " + str(article_id) + "Found: " + str(article_author_content.article_id))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()