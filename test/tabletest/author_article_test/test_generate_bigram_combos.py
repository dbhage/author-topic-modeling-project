'''
Created on Oct 21, 2014

@author: dbhage

Module to test table.author_article.generate_bigram_combos(...) functions.
'''

import unittest

from table.author_article import generate_bigram_combos

class TestGenerateBigramCombos(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Author invalid
        '''
        author = None
        ignore_list = ["the"]
        self.assertRaises(ValueError, generate_bigram_combos, author, ignore_list)

    def test_case2(self):
        '''
        TC2: Invalid case. ignore list None
        '''
        author = AuthorStub([],[])
        ignore_list = None
        self.assertRaises(ValueError, generate_bigram_combos, author, ignore_list)

    def test_case3(self):
        '''
        TC3: 1 bigram, no ignore list
        '''
        author = AuthorStub(["Dean"],["Neerav"])
        ignore_list = []
        actual = generate_bigram_combos(author, ignore_list)
        expected = ["Dean Neerav"]
        self.assertEqual(actual, expected)

    def test_case4(self):
        '''
        TC4: 1 bigram, ignore list
        '''
        author = AuthorStub(["Dean", "the"],["Neerav", "of"])
        ignore_list = ["the", "of"]
        actual = generate_bigram_combos(author, ignore_list)
        expected = ["Dean Neerav"]
        self.assertEqual(actual, expected)
        
    def test_case5(self):
        '''
        TC5: 2 bigrams, ignore list
        '''
        author = AuthorStub(["Dean", "the"],["Neerav", "of", "Bhageerutty"])
        ignore_list = ["the", "of"]
        actual = generate_bigram_combos(author, ignore_list)
        expected = ["Dean Neerav", "Dean Bhageerutty"]
        self.assertEqual(actual, expected)

    def test_case6(self):
        '''
        TC6: author has no last name
        '''
        author = AuthorStub(["Dean", "the"],[])
        ignore_list = ["the", "of"]
        actual = generate_bigram_combos(author, ignore_list)
        expected = []
        self.assertEqual(actual, expected)

    def test_case7(self):
        '''
        TC7: author has no first name
        '''
        author = AuthorStub([],["bhageerutty"])
        ignore_list = ["the", "of"]
        actual = generate_bigram_combos(author, ignore_list)
        expected = []
        self.assertEqual(actual, expected)

class AuthorStub(object):
    '''
    Author class stub to pass to function
    '''
    def __init__(self, fnames, lnames):
        self.first_names = fnames
        self.last_names = lnames

if __name__ == "__main__":
    unittest.main()