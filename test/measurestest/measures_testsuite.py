'''
Created on Jul 17, 2014

@author: dbhage
'''

from anr_test.test_article_author_content_add_mention import TestArticleAuthorContentAddMention
from anr_test.test_article_author_content_constructor import TestArticleAuthorContentConstructor
from anr_test.test_article_author_content_get_author_list import TestArticleAuthorContentGetAuthorList

from anr_test.test_get_validated_data import TestGetValidatedData

from entropytest.test_formula_inside_sum import TestFormulaInsideSum
from entropytest.test_no_docs_with_topics import TestNoOfDocsWithTopics
from entropytest.test_entropy_summation import TestEntropySummation

from commontest.test_get_docs_per_author import TestGetDocsPerAuthor

from author_articles_test.calculations_test import TestGetNoOfArticles, TestGetNoOfArticlesWithAtLeastNAuthors, TestGetPercentageOfArticlesWith2Languages, TestGetPercentageOfArticlesWith2Languages2Authors

import unittest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([TestArticleAuthorContentAddMention(),
                         TestArticleAuthorContentConstructor(),
                         TestArticleAuthorContentGetAuthorList(),
                         TestGetValidatedData(),
                         TestFormulaInsideSum(),
                         TestNoOfDocsWithTopics(),
                         TestEntropySummation(),
                         TestGetDocsPerAuthor(),
                         TestGetNoOfArticles(),
                         TestGetNoOfArticlesWithAtLeastNAuthors(),
                         TestGetPercentageOfArticlesWith2Languages(),
                         TestGetPercentageOfArticlesWith2Languages2Authors()])

if __name__ == '__main__':
    unittest.runner.TextTestRunner(suite()).run()