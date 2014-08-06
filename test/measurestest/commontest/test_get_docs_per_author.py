'''
Created on Aug 6, 2014

@author: dbhage
'''

import unittest

from measures.common import get_documents_per_author

class TestGetDocsPerAuthor(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Input None
        '''
        author_articles = None
        actual = get_documents_per_author(author_articles)
        self.assertIsNone(actual, "None input shoud return none")

    def test_case2(self):
        '''
        TC2: Invalid case. Input empty dict
        '''
        author_articles = dict()
        actual = get_documents_per_author(author_articles)
        self.assertIsNone(actual, "None input shoud return none")

    def test_case3(self):
        '''
        TC3: Valid case. Input one element with one article and one author
        '''
        author_articles = {"article 1" : [AuthorStub(["dean"], ["neerav"])]}
        actual = get_documents_per_author(author_articles)
        expected = {AuthorStub(["dean"], ["neerav"]) : 1}
        self.assertDictEqual(actual, expected, "dicts do not match")
        
    def test_case4(self):
        '''
        TC4: Valid case. Input one element with one article and 2 authors
        '''
        author_articles = {"article 1" : [AuthorStub(["dean"], ["neerav"]), AuthorStub(["bo"], ["ob"])]}
        actual = get_documents_per_author(author_articles)
        expected = {AuthorStub(["dean"], ["neerav"]) : 1, AuthorStub(["bo"], ["ob"]) : 1}
        self.assertDictEqual(actual, expected, "dicts do not match")
    
    def test_case5(self):
        '''
        TC5: Valid case. Input one element with 2 articles and 1 author
        '''
        author_articles = {"article 1" : [AuthorStub(["dean"], ["neerav"])], "article 2" : [AuthorStub(["dean"], ["neerav"])]}
        actual = get_documents_per_author(author_articles)
        expected = {AuthorStub(["dean"], ["neerav"]) : 2}
        self.assertDictEqual(actual, expected, "dicts do not match")

    def test_case6(self):
        '''
        TC6: Valid case. Input one element with 2 articles and 2 authors
        '''
        author_articles = {"article 1" : [AuthorStub(["dean"], ["neerav"])], "article 2" : [AuthorStub(["dean"], ["neerav"]), AuthorStub(["po"], ["op"])]}
        actual = get_documents_per_author(author_articles)
        expected = {AuthorStub(["dean"], ["neerav"]) : 2, AuthorStub(["po"], ["op"]) : 1}
        self.assertDictEqual(actual, expected, "dicts do not match")
    
    def test_case7(self):
        '''
        TC7: Valid case. No authors
        '''
        author_articles = {"article 1" : [], "article 2" : []}
        actual = get_documents_per_author(author_articles)
        expected = {}
        self.assertDictEqual(actual, expected, "dicts do not match")
    
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