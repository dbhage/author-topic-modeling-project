'''
Created on Jun 25, 2014

@author: dbhage

Test author.names.find_dot_pattern function.
'''

import unittest

from author.names import find_dot_pattern

class TestFindDotPattern(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Input: None
        '''
        text = None
        actual = find_dot_pattern(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
    def test_case2(self):
        '''
        TC2: Invalid case: Input: empty string
        '''
        text = ""
        actual = find_dot_pattern(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case3(self):
        '''
        TC3: valid case. Input: "M.D."
        '''
        text = "M.D."
        actual = find_dot_pattern(text)
        expected = [text]
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case4(self):
        '''
        TC4: Valid case. Pattern not present. Input: "popo...popo"
        '''
        text = "popo...popo"
        actual = find_dot_pattern(text)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

if __name__ == "__main__":
    unittest.main()