'''
Created on Jul 17, 2014

@author: dbhage
'''

import unittest

from measures.author_name_recognition import ArticleAuthorContent

class TestArticleAuthorContentAddMention(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. Add an author with significance True, then the same author with significance False
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = True
        aac.add_mention(author, significant)
        
        author = "Dean"
        significant = False
        self.assertRaises(ValueError, aac.add_mention, author, significant)

    def test_case2(self):
        '''
        TC2: Invalid case. Add an author with significance False, then the same author with significance True
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = False
        aac.add_mention(author, significant)
        
        author = "Dean"
        significant = True
        self.assertRaises(ValueError, aac.add_mention, author, significant)

    def test_case3(self):
        '''
        TC3: Invalid case. Add an author with significance True, add something else, then the 1st author with significance False
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = True
        aac.add_mention(author, significant)

        author = "Neerav"
        significant = True
        aac.add_mention(author, significant)

        author = "Dean"
        significant = False
        self.assertRaises(ValueError, aac.add_mention, author, significant)

    def test_case4(self):
        '''
        TC4: Invalid case. Add an author with significance False, add something else, then the 1st author with significance True
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = False
        aac.add_mention(author, significant)

        author = "neerav"
        significant = False
        aac.add_mention(author, significant)
        
        author = "Dean"
        significant = True
        self.assertRaises(ValueError, aac.add_mention, author, significant)

    def test_case5(self):
        '''
        TC5: Valid Case. Add non significant author
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = False
        aac.add_mention(author, significant)
        expected_dict = {author:significant}

        self.assertEqual(expected_dict, aac.mentions, "Dicts do not match")

    def test_case6(self):
        '''
        TC6: Valid Case. Add significant author
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = True
        aac.add_mention(author, significant)
        expected_dict = {author:significant}

        self.assertEqual(expected_dict, aac.mentions, "Dicts do not match")

    def test_case7(self):
        '''
        TC7: Valid Case. Add 2 different authors
        '''
        aac = ArticleAuthorContent(223)
        
        author = "Dean"
        significant = True
        aac.add_mention(author, significant)
        
        expected_dict = {author:significant}

        author = "Neerav"
        significant = False
        aac.add_mention(author, significant)

        expected_dict[author] = significant

        self.assertEqual(expected_dict, aac.mentions, "Dicts do not match")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()