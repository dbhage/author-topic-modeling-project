'''
Created on Jul 10, 2014

@author: dbhage
'''

import unittest
from datetime import date
from corpus.jstor.citations_parser import get_citation

class TestGetCitation(unittest.TestCase):
    
    def test_case1(self):
        '''
        TC1: Invalid case: line is None
        '''
        line = None
        citation = CitationStub()
        actual = get_citation(line, citation)
        self.assertIsNone(actual, "Expected none")
        
    def test_case2(self):
        '''
        TC2: Invalid case: line is ''
        '''
        line = ""
        citation = CitationStub()
        actual = get_citation(line, citation)
        self.assertIsNone(actual, "Expected none")

    def test_case3(self):
        '''
        TC3: Invalid case: citation is None
        '''
        line = "10.2307/3885944,10.2307/3885944    ,The Social Construct of Enthymematic Understanding    ,J. Scenters-Zapico    ,Rhetoric Society Quarterly    ,24    ,3/4    ,1994-07-01T00:00:00Z    ,pp. 71-87    ,Taylor & Francis_ Ltd.    ,fla    ,    ,"
        citation = None
        actual = get_citation(line, citation)
        self.assertIsNone(actual, "Expected none")

    def test_case4(self):
        '''
        TC4: Invalid case: Volume not an int. Should raise ValueError.
        '''
        line = "10.2307/3885944,10.2307/3885944    ,The Social Construct of Enthymematic Understanding    ,J. Scenters-Zapico    ,Rhetoric Society Quarterly    ,2a4    ,3/4    ,1994-07-01T00:00:00Z    ,pp. 71-87    ,Taylor & Francis_ Ltd.    ,fla    ,    ,"
        citation = CitationStub()
        self.assertRaises(ValueError, get_citation, line,citation)

    def test_case5(self):
        '''
        TC5: Valid case. Valid line and citation.
        '''
        line = "10.2307/3885944,10.2307/3885944    ,The Social Construct of Enthymematic Understanding    ,J. Scenters-Zapico    ,Rhetoric Society Quarterly    ,24    ,3/4    ,1994-07-01T00:00:00Z    ,pp. 71-87    ,Taylor & Francis_ Ltd.    ,fla    ,    ,"

        citation = CitationStub()
        citation = get_citation(line, citation)
        
        self.assertIsNotNone(citation, "Citation should not be None.")
        
        expected = "10.2307/3885944"
        actual = citation.id
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "10.2307/3885944    "
        actual = citation.doi
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "The Social Construct of Enthymematic Understanding    "
        actual = citation.title
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "J. Scenters-Zapico    "
        actual = citation.author
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "Rhetoric Society Quarterly    "
        actual = citation.journal_title
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
        expected = 24
        actual = citation.volume
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
        expected = "Rhetoric Society Quarterly    "
        actual = citation.journal_title
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "3/4    "
        actual = citation.issue
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1994
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 7
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "pp. 71-87    "
        actual = citation.page_range
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
        expected = "Taylor & Francis_ Ltd.    "
        actual = citation.publisher
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = "fla    "
        actual = citation.type
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
class CitationStub(object):
    '''
    Citation Stub class
    '''
    def __init__(self):
        '''
        Initialise members
        '''        
        self.id = ""
        self.doi = ""
        self.title = ""
        self.author = ""
        self.journal_title = ""
        self.volume = -1
        self.issue = ""
        self.pub_date = None
        self.page_range = ""
        self.publisher = ""
        self.type = ""
        self.reviewed_work = ""
    
    def set_pub_date(self, date_str):
        if date_str == "1994-07-01T00:00:00Z    ":
            self.pub_date = date(1994, 7, 1)

if __name__ == "__main__":
    unittest.main()