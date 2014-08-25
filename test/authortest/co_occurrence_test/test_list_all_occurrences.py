'''
Created on Aug 25, 2014

@author: dbhage
'''

import unittest

from author.co_occurrence.co_occurrence import list_all_co_occurences

class TestListAllCoOccurrences(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Empty List
        '''
        author_list = []
        actual_list = list_all_co_occurences(author_list)
        self.assertIsNone(actual_list)

    def test_case2(self):
        '''
        TC2: Invalid case. Input None
        '''
        author_list = None
        actual_list = list_all_co_occurences(author_list)
        self.assertIsNone(actual_list)

    def test_case3(self):
        '''
        TC3: Valid case. Input one author
        '''
        author_list = [AuthorStub("f", "l")]
        expected_list = []
        actual_list = list_all_co_occurences(author_list)
        self.assertEquals(expected_list, actual_list, "Expected: " + str(expected_list) + ", Actual: " + str(actual_list))

    def test_case4(self):
        '''
        TC4: Valid case. Input one author
        '''
        author_list = [AuthorStub("f", "l")]
        expected_list = []
        actual_list = list_all_co_occurences(author_list)
        self.assertEquals(expected_list, actual_list, "Expected: " + str(expected_list) + ", Actual: " + str(actual_list))

    def test_case5(self):
        '''
        TC5: Valid case. Input 2 authors
        '''
        author_list = [AuthorStub("f", "l"), AuthorStub("f1", "l1")]

        actual_list = list_all_co_occurences(author_list)
        
        self.assertEquals(len(actual_list), 1)
        self.assertEquals(actual_list[0].author1, author_list[0])
        self.assertEquals(actual_list[0].author2, author_list[1])

    def test_case6(self):
        '''
        TC6: Valid case. Input 3 authors
        '''
        author_list = [AuthorStub("f", "l"), AuthorStub("f1", "l1"), AuthorStub("f2", "l2")]

        actual_list = list_all_co_occurences(author_list)
        
        self.assertEquals(len(actual_list), 3)
        
        self.assertEquals(actual_list[0].author1, author_list[0])
        self.assertEquals(actual_list[0].author2, author_list[1])

        self.assertEquals(actual_list[1].author1, author_list[0])
        self.assertEquals(actual_list[1].author2, author_list[2])
        
        self.assertEquals(actual_list[2].author1, author_list[1])
        self.assertEquals(actual_list[2].author2, author_list[2])

class AuthorStub(object):
    def __init__(self, fnames, lnames):
        self.first_names = fnames
        self.last_names = lnames
    
    def __str__(self):
        return  ' '.join(self.first_names) + " " + ' '.join(self.last_names)
    
    def __eq__(self, other):
        return other.first_names == self.first_names and other.last_names == self.last_names
    
    def __hash__(self):
        return hash((''.join(self.first_names), ''.join(self.last_names)))

if __name__ == "__main__":
    unittest.main()