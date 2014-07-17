'''
Created on Jul 17, 2014

@author: dbhage
'''

from anr_test.test_article_author_content_add_mention import TestArticleAuthorContentAddMention
from anr_test.test_article_author_content_constructor import TestArticleAuthorContentConstructor
from anr_test.test_article_author_content_get_author_list import TestArticleAuthorContentGetAuthorList

import unittest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([TestArticleAuthorContentAddMention(),
                         TestArticleAuthorContentConstructor(),
                         TestArticleAuthorContentGetAuthorList()])

if __name__ == '__main__':
    unittest.runner.TextTestRunner(suite()).run()