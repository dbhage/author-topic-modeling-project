'''
Created on Oct 22, 2014

@author: dbhage
'''

import unittest

from table.author_article import name_bigram_present

class TestNameBigramPresent(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: invalid case. bigram combos None
        '''
        bigram_combos = None
        article_content = "this is an article"
        self.assertRaises(ValueError, name_bigram_present, bigram_combos, article_content)

    def test_case2(self):
        '''
        TC2: invalid case. article content none
        '''
        bigram_combos = []
        article_content = None
        self.assertRaises(ValueError, name_bigram_present, bigram_combos, article_content)
        
    def test_case3(self):
        '''
        TC3: invalid case. article content empty
        '''
        bigram_combos = []
        article_content = ''
        self.assertRaises(ValueError, name_bigram_present, bigram_combos, article_content)

    def test_case4(self):
        '''
        TC4: valid case. bigram not present
        '''
        bigram_combos = ["dean ovich"]
        article_content = "this is an article with no bigrams"
        self.assertFalse(name_bigram_present(bigram_combos, article_content))
    
    def test_case5(self):
        '''
        TC5: valid case. bigram present
        '''
        bigram_combos = ["dean ovich"]
        article_content = "this is an article about dean ovich"
        self.assertTrue(name_bigram_present(bigram_combos, article_content))
    
    def test_case6(self):
        '''
        TC6: valid case. bigram present
        '''
        bigram_combos = ["dean ovich"]
        article_content = "this is an article about \ndean ovich\n"
        self.assertTrue(name_bigram_present(bigram_combos, article_content))

    def test_case7(self):
        '''
        TC7: valid case. bigram present but as part of other bigram so should return false
        '''
        bigram_combos = ["dean ovich"]
        article_content = "this is an article about \ndean ovichasamy\n"
        self.assertFalse(name_bigram_present(bigram_combos, article_content))

if __name__ == "__main__":
    unittest.main()