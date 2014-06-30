'''
Created on Jun 25, 2014

@author: dbhage
'''

import unittest

from author.author import get_authors
from author.author import Author

class TestGetAuthors(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Input: None
        '''
        lines = None
        actual = get_authors(lines)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case2(self):
        '''
        TC2: Invalid case. Input: []
        '''
        lines = []
        actual = get_authors(lines)
        expected = []
        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
    def test_case_3(self):
        '''
        TC3: Valid Case. 1 comma, just names
        '''
        lines = ["Aguilar,Grace"]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = ["grace"]
        expected_author.last_names = ["aguilar"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_4(self):
        '''
        TC4: Valid Case. 2 commas, just names
        '''
        lines = ["Aguilar,Grace,Bibu"]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = ["grace", "bibu"]
        expected_author.last_names = ["aguilar"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_5(self):
        '''
        TC5: Valid Case. 0 commas, just one name
        '''
        lines = ["Aguilar"]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = []
        expected_author.last_names = ["aguilar"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_6(self):
        '''
        TC6: Valid Case. 0 commas, just one name
        '''
        lines = ["Aguilar"]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = []
        expected_author.last_names = ["aguilar"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_7(self):
        '''
        TC7: 1 comma, name + initials
        '''
        lines = ["Barrie,J.M."]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = ["j.m."]
        expected_author.last_names = ["barrie"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_8(self):
        '''
        TC8: 1 comma , multiple names in first name
        '''
        lines = ["Bhageerutty, DwijeshDeanNeerav"]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = ["dwijesh", "dean", "neerav"]
        expected_author.last_names = ["bhageerutty"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_9(self):
        '''
        TC9: 2 commas, 1 last name, 2 first names. Ends in a comma. 
        '''
        lines = ["Ramuz,CharlesFerdinand,"]
        authors = get_authors(lines)
        
        expected_author = Author()
        expected_author.first_names = ["charles", "ferdinand"]
        expected_author.last_names = ["ramuz"]
        
        actual = authors[0]
        expected = expected_author

        self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case_10(self):
        '''
        TC10: 2 lines
        '''
        lines = ["Ramuz,M.D. ,", "Bhageerutty, DwijeshDeanNeerav"]
        authors = get_authors(lines)
        
        expected_author = []
        expected_author.append(Author())
        expected_author.append(Author())
        expected_author[0].first_names = ["m.d."]
        expected_author[0].last_names = ["ramuz"]
        expected_author[1].first_names = ["dwijesh", "dean", "neerav"]
        expected_author[1].last_names = ["bhageerutty"]

        for i in [0,1]:        
            actual = authors[i]
            expected = expected_author[i]
            self.assertEquals(expected, actual, "Expected: " + str(expected) + " Actual: " + str(actual))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()