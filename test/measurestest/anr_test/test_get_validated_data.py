'''
Created on Jul 22, 2014

@author: dbhage
'''
import unittest

from measures.author_name_recognition import get_validated_data
from author.author import Author

class TestGetValidatedData(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. lines is None.
        '''
        lines = None
        actual = get_validated_data(lines)
        self.assertIsNone(actual, "Expected None")
        
    def test_case2(self):
        '''
        TC2: Invalid case. lines is [].
        '''
        lines = []
        actual = get_validated_data(lines)
        self.assertIsNone(actual, "Expected None")

    def test_case3(self):
        '''
        TC3: Valid. One line.
        '''
        lines = ["456789, Twain, Marc, Yes, blablabla, blublublu"]
        actual_dict = get_validated_data(lines)

        expected_author = Author()
        expected_author.first_names = ["marc"]
        expected_author.last_names = ["twain"]

        self.assertEqual(actual_dict.keys()[0], "456789", "ids do not match")
        
        actual_aac = actual_dict["456789"]
        actual_author = actual_aac.get_author_list()[0]
        self.assertEqual(actual_author, expected_author, "Expected: " + str(expected_author) + " Found:" + str(actual_author))

        actual_author = actual_aac.get_significant_author_list()[0]
        self.assertEqual(actual_author, expected_author, "Expected: " + str(expected_author) + " Found:" + str(actual_author))
        
        self.assertTrue(actual_aac.mentions[actual_author], "significance should be true")

    # TODO: add test with 2 lines

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()
    
    
    
