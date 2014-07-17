'''
Created on Jul 12, 2014

@author: dbhage
'''

import unittest

from authortest.test_get_authors import TestGetAuthors
from authortest.namestest.test_extract_author_names import TestExtractAuthorNames
from authortest.namestest.test_find_dot_pattern import TestFindDotPattern
from authortest.namestest.test_find_upper_lowers_pattern import TestFindUpperLowersPattern

from corpustest.jstortest.test_citation import TestCitationSetPubDate
from corpustest.jstortest.test_get_citation import TestGetCitation

from tabletest.author_article_test.test_author_article_lnop import TestAuthorArticleLNOP
from tabletest.author_article_test.test_author_article_lnaofnp import TestAuthorArticleLNAOFNP
from tabletest.author_article_test.test_author_article_fnp import TestAuthorArticleFNP
from tabletest.author_article_test.test_find_authors import TestAuthorArticleFindAuthor

def suite():
    suite = unittest.TestSuite()
    suite.addTests([TestFindDotPattern(), TestFindUpperLowersPattern(), TestExtractAuthorNames(), TestGetAuthors()])
    suite.addTests([TestCitationSetPubDate(), TestGetCitation()])
    suite.addTests([TestAuthorArticleFindAuthor(), TestAuthorArticleFNP(), TestAuthorArticleLNAOFNP(), TestAuthorArticleLNOP()])
    return suite

if __name__=="__main__":
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)