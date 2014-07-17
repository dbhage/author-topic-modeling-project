'''
Created on Jul 17, 2014

@author: dbhage

Test measures.author_name_recognition.ArticleAuthorContent.get_author_list
Test measures.author_name_recognition.ArticleAuthorContent.get_significant_author_list
'''

import unittest

from measures.author_name_recognition import ArticleAuthorContent

class TestArticleAuthorContentGetAuthorList(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Test get_author_list right after init
        '''
        aac = ArticleAuthorContent(889)
        
        self.assertListEqual(aac.get_author_list(), [])
    
    def test_case2(self):
        '''
        TC2: Test get_author_list with several authors
        '''
        aac = ArticleAuthorContent(334)

        authors = ["dean", "neerav", "po"]

        author_sig_list = [(authors[0], True), (authors[1], True), (authors[2], False)]

        for (auth, sig) in author_sig_list:
            aac.mentions[auth] = sig
        
        self.assertListEqual(authors, aac.get_author_list())
    
    def test_case3(self):
        '''
        TC3: Test get_significant_author_list right after init
        '''
        aac = ArticleAuthorContent(889)
        
        self.assertListEqual(aac.get_significant_author_list(), [])

    def test_case4(self):
        '''
        TC4: Test get_significant_author_list with all significant authors
        '''
        aac = ArticleAuthorContent(334)

        authors_true = ["dean", "neerav", "po"]
        authors_false = []

        for auth in authors_true:
            aac.mentions[auth] = True
        for auth in authors_false:
            aac.mentions[auth] = False
        
        self.assertListEqual(authors_true, aac.get_significant_author_list())

    def test_case5(self):
        '''
        TC5: Test get_significant_author_list with no significant authors
        '''
        aac = ArticleAuthorContent(334)

        authors_false = ["dean", "neerav", "po"]
        authors_true = []

        for auth in authors_true:
            aac.mentions[auth] = True
        for auth in authors_false:
            aac.mentions[auth] = False
        
        self.assertListEqual([], aac.get_significant_author_list())

    def test_case6(self):
        '''
        TC6: Test get_significant_author_list with both sig and non sig auths
        '''
        aac = ArticleAuthorContent(334)

        authors_false = ["dean", "neerav", "po"]
        authors_true = ["bobo", "baba"]

        for auth in authors_true:
            aac.mentions[auth] = True
        for auth in authors_false:
            aac.mentions[auth] = False
        
        self.assertListEqual(authors_true, aac.get_significant_author_list())
    
if __name__ == "__main__":
    unittest.main()