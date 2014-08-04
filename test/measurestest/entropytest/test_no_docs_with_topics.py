'''
Created on Aug 3, 2014

@author: dbhage
'''

import unittest

from measures.entropy import no_of_docs_with_topic

class TestNoOfDocsWithTopics(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case: dict none
        '''
        compositions = None
        actual = no_of_docs_with_topic(compositions)
        self.assertIsNone(actual, "Expected none")

    def test_case2(self):
        '''
        TC2: Invalid case: dict empty
        '''
        compositions = dict()
        actual = no_of_docs_with_topic(compositions)
        self.assertIsNone(actual, "Expected none")

    def test_case3(self):
        '''
        TC3: Valid case: dict with one doc
        '''
        compositions = {"doc1": CompositionStub(1)}
        actual = no_of_docs_with_topic(compositions)
        expected = {1:1}
        
        self.assertDictEqual(actual, expected, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case4(self):
        '''
        TC4: Valid case: dict with 2 docs, 1 topic
        '''
        compositions = {"doc1": CompositionStub(1), "doc2": CompositionStub(1)}
        actual = no_of_docs_with_topic(compositions)
        expected = {1:2}
        
        self.assertDictEqual(actual, expected, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case5(self):
        '''
        TC5: Valid case: dict with 2 docs 2 topics
        '''
        compositions = {"doc1": CompositionStub(1), "doc2": CompositionStub(18)}
        actual = no_of_docs_with_topic(compositions)
        expected = {1:1, 18:1}
        
        self.assertDictEqual(actual, expected, "Expected: " + str(expected) + " Actual: " + str(actual))

class CompositionStub(object):
    def __init__(self, main_topic):
        self.main_topic = main_topic

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()