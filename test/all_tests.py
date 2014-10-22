'''
Created on Jul 12, 2014

@author: dbhage

Main Test Suite
'''

import unittest

from authortest.test_get_authors import TestGetAuthors
from authortest.namestest.test_extract_author_names import TestExtractAuthorNames
from authortest.namestest.test_find_dot_pattern import TestFindDotPattern
from authortest.namestest.test_find_upper_lowers_pattern import TestFindUpperLowersPattern

from authortest.co_occurrence_test.test_list_all_occurrences import TestListAllCoOccurrences
from authortest.co_occurrence_test.test_get_co_occurrence_dict import TestGetCoOccurrenceDict

from tabletest.author_article_test.test_author_article_lnop import TestAuthorArticleLNOP
from tabletest.author_article_test.test_author_article_lnaofnp import TestAuthorArticleLNAOFNP
from tabletest.author_article_test.test_author_article_fnp import TestAuthorArticleFNP

from measurestest.anr_test.test_article_author_content_add_mention import TestArticleAuthorContentAddMention
from measurestest.anr_test.test_article_author_content_constructor import TestArticleAuthorContentConstructor
from measurestest.anr_test.test_article_author_content_get_author_list import TestArticleAuthorContentGetAuthorList
from measurestest.anr_test.test_get_validated_data import TestGetValidatedData
from measurestest.entropytest.test_formula_inside_sum import TestFormulaInsideSum
from measurestest.entropytest.test_no_docs_with_topics import TestNoOfDocsWithTopics
from measurestest.entropytest.test_entropy_summation import TestEntropySummation
from measurestest.commontest.test_get_docs_per_author import TestGetDocsPerAuthor
from measurestest.author_articles_test.calculations_test import TestGetNoOfArticles, TestGetNoOfArticlesWithAtLeastNAuthors, TestGetPercentageOfArticlesWith2Languages, TestGetPercentageOfArticlesWith2Languages2Authors

from tabletest.author_topic_test.test_author_topic_class import TestAuthorTopicClass
from tabletest.author_article_test.test_generate_bigram_combos import TestGenerateBigramCombos
from tabletest.author_article_test.test_get_last_name_count import TestGetLastNameCount
from tabletest.author_article_test.test_name_bigram_present import TestNameBigramPresent

def suite():
    suite = unittest.TestSuite()
    
    suite.addTests([TestFindDotPattern(), 
                    TestFindUpperLowersPattern(), 
                    TestExtractAuthorNames(), 
                    TestGetAuthors(), 
                    TestAuthorArticleFNP(), 
                    TestAuthorArticleLNAOFNP(), 
                    TestAuthorArticleLNOP(),
                    TestArticleAuthorContentAddMention(), 
                    TestArticleAuthorContentConstructor(), 
                    TestArticleAuthorContentGetAuthorList(), 
                    TestGetValidatedData(), 
                    TestFormulaInsideSum(), 
                    TestNoOfDocsWithTopics(), 
                    TestEntropySummation(), 
                    TestAuthorTopicClass(),
                    TestGetDocsPerAuthor(), 
                    TestListAllCoOccurrences(), 
                    TestGetCoOccurrenceDict(),
                    TestGetNoOfArticles(), 
                    TestGetNoOfArticlesWithAtLeastNAuthors(),
                    TestGetPercentageOfArticlesWith2Languages(), 
                    TestGetPercentageOfArticlesWith2Languages2Authors(),
                    TestGenerateBigramCombos(),
                    TestGetLastNameCount(),
                    TestNameBigramPresent()])

    return suite

if __name__=="__main__":
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)