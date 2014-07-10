'''
Created on Jul 10, 2014

@author: dbhage
'''

import unittest

from jstortest.test_citation import TestCitationSetPubDate
from jstortest.test_get_citation import TestGetCitation

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([TestCitationSetPubDate(), TestGetCitation()])

if __name__ == '__main__':
    test_suite = suite()
    unittest.runner.TextTestRunner().run(test_suite)