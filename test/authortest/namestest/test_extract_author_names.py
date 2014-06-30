'''
Created on Jun 25, 2014

@author: dbhage
'''

import unittest

from author.names import extract_author_names

class TestExtractAuthorNames(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Input: None
        '''
        text = None
        actual = extract_author_names(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case2(self):
        '''
        TC2: Invalid case. Input: empty string
        '''
        text = ""
        actual = extract_author_names(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case3(self):
        '''
        TC3: Valid case. Input: "Mr.DwijeshBhageerutty"
        '''
        text = "Mr.DwijeshBhageerutty"
        actual = extract_author_names(text)
        expected = ["Dwijesh", "Bhageerutty"]
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
    def test_case4(self):
        '''
        TC4: Valid case. Input: "Mrs. Bibu"
        '''
        text = "Mrs. Bibu"
        actual = extract_author_names(text)
        expected = ["Bibu"]
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case5(self):
        '''
        TC5: Valid case. Input: "M.D."
        '''
        text = "M.D."
        actual = extract_author_names(text)
        expected = ["M.D."]
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()