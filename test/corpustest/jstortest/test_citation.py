'''
Created on Jul 10, 2014

@author: dbhage
'''

import unittest
from corpus.jstor.citations_parser import Citation

class TestCitationSetPubDate(unittest.TestCase):
    '''
    Test Citation.set_pub_date function.
    '''
    def test_case1(self):
        '''
        TC1: Invalid Case: Input is None
        '''
        citation = Citation()
        date_str = None
        citation.set_pub_date(date_str)
        
        self.assertIsNone(citation.pub_date, "pub_date should be None")

    def test_case2(self):
        '''
        TC2: Invalid Case: Input is ''
        '''
        citation = Citation()
        date_str = ""
        citation.set_pub_date(date_str)
        
        self.assertIsNone(citation.pub_date, "pub_date should be None")

    def test_case3(self):
        '''
        TC3: Valid Case: Input string contains a valid date
        '''
        citation = Citation()
        date_str = "1993-01-02"
        citation.set_pub_date(date_str)
        
        expected = 2
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1993
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case4(self):
        '''
        TC4: Valid Case: Input string contains a valid date plus garbage at the end
        '''
        citation = Citation()
        date_str = "1993-01-02Tjbvuejbveob"
        citation.set_pub_date(date_str)
        
        expected = 2
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1993
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case5(self):
        '''
        TC5: Valid Case: Input string contains a valid date plus garbage at the beginning
        '''
        citation = Citation()
        date_str = "sdjk jbjdk s1993-01-02"
        citation.set_pub_date(date_str)
        
        expected = 2
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1993
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case6(self):
        '''
        TC6: Valid Case: Input string contains a valid date plus garbage on both sides
        '''
        citation = Citation()
        date_str = "jcdksn ojdp 1993-01-02 cjbvuejbveob"
        citation.set_pub_date(date_str)
        
        expected = 2
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1993
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case7(self):
        '''
        TC7: Valid Case: Input string contains 2 dates
        '''
        citation = Citation()
        date_str = "1993-01-02 2002-01-02"
        citation.set_pub_date(date_str)
        
        expected = 2
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1993
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case8(self):
        '''
        TC8: Valid Case: Input string contains 2 dates plus garbage
        '''
        citation = Citation()
        date_str = "kjksbvkjf1993-01-02 cjbsdkvj 2002-01-02 jkdsbvdjks"
        citation.set_pub_date(date_str)
        
        expected = 2
        actual = citation.pub_date.day
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1
        actual = citation.pub_date.month
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

        expected = 1993
        actual = citation.pub_date.year
        self.assertEqual(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()