'''
Created on Jun 25, 2014

@author: dbhage

Test Suite for author package
'''

import unittest

from test_get_authors import TestGetAuthors

from authortest.namestest.test_extract_author_names import TestExtractAuthorNames
from authortest.namestest.test_find_dot_pattern import TestFindDotPattern
from authortest.namestest.test_find_upper_lowers_pattern import TestFindUpperLowersPattern

from authortest.co_occurrence_test.test_list_all_occurrences import TestListAllCoOccurrences
from authortest.co_occurrence_test.test_get_co_occurrence_dict import TestGetCoOccurrenceDict

def suite():
    suite = unittest.TestSuite()
    
    suite.addTests([TestFindDotPattern(), 
                    TestFindUpperLowersPattern(), 
                    TestExtractAuthorNames(), 
                    TestGetAuthors(),
                    TestListAllCoOccurrences(),
                    TestGetCoOccurrenceDict()])

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)