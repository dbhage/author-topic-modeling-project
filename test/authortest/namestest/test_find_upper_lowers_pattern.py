'''
Created on Jun 25, 2014

@author: dbhage
'''

import unittest

from author.names import find_upper_lowers_pattern

class TestFindUpperLowersPattern(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Input: None
        '''
        text = None
        actual = find_upper_lowers_pattern(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
    def test_case2(self):
        '''
        TC2: Invalid case: Input: empty string
        '''
        text = ""
        actual = find_upper_lowers_pattern(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case3(self):
        '''
        TC3: Valid Case: Input: "DidierDeschamps"
        '''
        text = "DidierDeschamps"
        actual = find_upper_lowers_pattern(text)
        expected = ["Didier", "Deschamps"]
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case4(self):
        '''
        TC4: Valid Case: Input: "DidierDeschampsLeBoss"
        '''
        text = "DidierDeschampsLeBoss"
        actual = find_upper_lowers_pattern(text)
        expected = ["Didier", "Deschamps", "Le", "Boss"]
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case5(self):
        '''
        TC5: Valid Case: Patter not present. Input: "didierdeschampsleboss"
        '''
        text = "didierdeschampsleboss"
        actual = find_upper_lowers_pattern(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()