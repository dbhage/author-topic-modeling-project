'''
Created on Jul 1, 2014

@author: dbhage
'''

import unittest

from author_article_test.test_author_article_lnop import TestAuthorArticleLNOP
from author_article_test.test_author_article_lnaofnp import TestAuthorArticleLNAOFNP
from author_article_test.test_author_article_fnp import TestAuthorArticleFNP
from author_article_test.test_find_authors import TestAuthorArticleFindAuthor

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([TestAuthorArticleFindAuthor(), 
                         TestAuthorArticleFNP(), 
                         TestAuthorArticleLNAOFNP(), 
                         TestAuthorArticleLNOP()])
    return test_suite

if __name__=="__main__":
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)