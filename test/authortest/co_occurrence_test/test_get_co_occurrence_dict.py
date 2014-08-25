'''
Created on Aug 25, 2014

@author: dbhage
'''

import unittest

from author.co_occurrence.co_occurrence import get_co_occurrence_dict

class TestGetCoOccurrenceDict(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Empty dict
        '''
        author_articles = dict()
        actual_dict = get_co_occurrence_dict(author_articles, list_all_co_occurrences_stub)
        self.assertIsNone(actual_dict)

    def test_case2(self):
        '''
        TC2: Invalid case. dict None
        '''
        author_articles = None
        actual_dict = get_co_occurrence_dict(author_articles, list_all_co_occurrences_stub)
        self.assertIsNone(actual_dict)

    def test_case3(self):
        '''
        TC3: Valid case. No co-occurrences
        '''
        author_articles = {"article1":[AuthorStub("f", "l")]}
        
        actual_dict = get_co_occurrence_dict(author_articles, list_all_co_occurrences_stub)
        expected_dict = {}
        
        self.assertDictEqual(actual_dict, expected_dict)

    def test_case4(self):
        '''
        TC4: Valid case. 1 co-occurrence present
        '''
        author_articles = {"article1" : [AuthorStub("f", "l"), AuthorStub("f1", "l1")]}
        
        actual_dict = get_co_occurrence_dict(author_articles, list_all_co_occurrences_stub)

        expected_dict = {CoOccurenceStub(AuthorStub("f", "l"), AuthorStub("f1", "l1")): 1}
        
        self.assertDictEqual(actual_dict, expected_dict)

    def test_case5(self):
        '''
        TC5: Valid case. 2 similar co-occurrences present
        '''
        author_articles = {"article1":[AuthorStub("f", "l"), AuthorStub("f1", "l1")], 
                           "article2":[AuthorStub("f", "l"), AuthorStub("f1", "l1")]}
        
        actual_dict = get_co_occurrence_dict(author_articles, list_all_co_occurrences_stub)

        expected_dict = {CoOccurenceStub(AuthorStub("f", "l"), AuthorStub("f1", "l1")): 2}
        
        self.assertDictEqual(actual_dict, expected_dict)

    def test_case6(self):
        '''
        TC6: Valid case. 2 different co-occurrences present
        '''
        author_articles = {"article1":[AuthorStub("f", "l"), AuthorStub("f1", "l1")], 
                           "article2":[AuthorStub("f", "l"), AuthorStub("f1", "l1"), AuthorStub("f2", "l2")]}
        
        actual_dict = get_co_occurrence_dict(author_articles, list_all_co_occurrences_stub)

        expected_dict = {CoOccurenceStub(AuthorStub("f", "l"), AuthorStub("f1", "l1")): 2,
                         CoOccurenceStub(AuthorStub("f", "l"), AuthorStub("f2", "l2")): 1,
                         CoOccurenceStub(AuthorStub("f1", "l1"), AuthorStub("f2", "l2")): 1}
        
        self.assertDictEqual(actual_dict, expected_dict)

def list_all_co_occurrences_stub(author_list):

    if author_list == [AuthorStub("f", "l"), AuthorStub("f1", "l1")]:
        return [CoOccurenceStub(author_list[0], author_list[1])]
    
    if author_list == [AuthorStub("f", "l"), AuthorStub("f1", "l1"), AuthorStub("f2", "l2")]:
        return [CoOccurenceStub(author_list[0], author_list[1]), 
                CoOccurenceStub(author_list[0], author_list[2]),
                CoOccurenceStub(author_list[1], author_list[2])]

class CoOccurenceStub(object):
    
    def __init__(self, auth1, auth2):
        self.author1 = auth1
        self.author2 = auth2

    def __hash__(self):
        return hash((self.author1, self.author2))

    def __eq__(self, other):
        return self.author1 == other.author1 or self.author2 == other.author2

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