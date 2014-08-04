'''
Created on Jul 1, 2014

@author: dbhage
'''

import unittest

from author_article_test.test_author_article_lnop import TestAuthorArticleLNOP
from author_article_test.test_author_article_lnaofnp import TestAuthorArticleLNAOFNP
from author_article_test.test_author_article_fnp import TestAuthorArticleFNP

from author_topic_test.test_author_topic_class import TestAuthorTopicClass

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([TestAuthorArticleFNP(), 
                         TestAuthorArticleLNAOFNP(), 
                         TestAuthorArticleLNOP(),
                         TestAuthorTopicClass()])
    return test_suite

if __name__=="__main__":
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)