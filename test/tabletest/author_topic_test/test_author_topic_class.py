'''
Created on Aug 4, 2014

@author: dbhage

Test table.author_topic.AuthorTopic class
'''

import unittest

from table.author_topic import AuthorTopic

class TestAuthorTopicClass(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: test constructor
        '''
        expected_author = AuthorStub(["dean"],["neerav"])
        expected_topic = 2
        author_topic = AuthorTopic(expected_author, 2)
        self.assertEqual(author_topic.author, expected_author, "Expected:" + str(expected_author) + " Actual: " + str(author_topic.author))
        self.assertEqual(author_topic.topic, 2, "Expected: " + str(expected_topic) + " Actual: " + str(author_topic.topic))

    def test_case2(self):
        '''
        TC2: test equality with 2 equal AuthorTopics
        '''
        expected_author = AuthorStub(["dean"],["neerav"])
        expected_topic = 2

        author_topic1 = AuthorTopic(expected_author, expected_topic)
        author_topic2 = AuthorTopic(expected_author, expected_topic)
        
        self.assertEquals(author_topic1, author_topic2, "__eq__ wrongly implemented")
        
    def test_case3(self):
        '''
        TC3: test equality with 2 unequal AuthorTopics with both different author and topic
        '''
        expected_author1 = AuthorStub(["dean"],["neerav"])
        expected_topic1 = 2

        expected_author2 = AuthorStub(["vsd"],["bibu"])
        expected_topic2 = 33

        author_topic1 = AuthorTopic(expected_author1, expected_topic1)
        author_topic2 = AuthorTopic(expected_author2, expected_topic2)
        
        self.assertNotEquals(author_topic1, author_topic2, "__eq__ wrongly implemented")
    
    def test_case4(self):
        '''
        TC4: test equality with 2 unequal AuthorTopics with different author and same topic
        '''
        expected_author1 = AuthorStub(["dean"],["neerav"])
        expected_topic1 = 33

        expected_author2 = AuthorStub(["vsd"],["bibu"])
        expected_topic2 = 33

        author_topic1 = AuthorTopic(expected_author1, expected_topic1)
        author_topic2 = AuthorTopic(expected_author2, expected_topic2)
        
        self.assertNotEquals(author_topic1, author_topic2, "__eq__ wrongly implemented")

    def test_case5(self):
        '''
        TC5: test equality with 2 unequal AuthorTopics with same author and different topic
        '''
        expected_author1 = AuthorStub(["dean"],["neerav"])
        expected_topic1 = 33

        expected_author2 = AuthorStub(["dean"],["neerav"])
        expected_topic2 = 90

        author_topic1 = AuthorTopic(expected_author1, expected_topic1)
        author_topic2 = AuthorTopic(expected_author2, expected_topic2)
        
        self.assertNotEquals(author_topic1, author_topic2, "__eq__ wrongly implemented")

    def test_case6(self):
        '''
        TC6: test equality with 2 equal AuthorTopics
        '''
        expected_author = AuthorStub(["dean"],["neerav"])
        expected_topic = 2

        author_topic1 = AuthorTopic(expected_author, expected_topic)
        author_topic2 = AuthorTopic(expected_author, expected_topic)
        
        self.assertEquals(author_topic1.__hash__(), author_topic2.__hash__(), "__hash__ wrongly implemented")
        
    def test_case7(self):
        '''
        TC7: test equality with 2 unequal AuthorTopics with both different author and topic
        '''
        expected_author1 = AuthorStub(["dean"],["neerav"])
        expected_topic1 = 2

        expected_author2 = AuthorStub(["vsd"],["bibu"])
        expected_topic2 = 33

        author_topic1 = AuthorTopic(expected_author1, expected_topic1)
        author_topic2 = AuthorTopic(expected_author2, expected_topic2)
        
        self.assertNotEquals(author_topic1.__hash__(), author_topic2.__hash__(), "__eq__ wrongly implemented")
    
    def test_case8(self):
        '''
        TC8: test equality with 2 unequal AuthorTopics with different author and same topic
        '''
        expected_author1 = AuthorStub(["dean"],["neerav"])
        expected_topic1 = 33

        expected_author2 = AuthorStub(["vsd"],["bibu"])
        expected_topic2 = 33

        author_topic1 = AuthorTopic(expected_author1, expected_topic1)
        author_topic2 = AuthorTopic(expected_author2, expected_topic2)
        
        self.assertNotEquals(author_topic1.__hash__(), author_topic2.__hash__(), "__eq__ wrongly implemented")

    def test_case9(self):
        '''
        TC9: test equality with 2 unequal AuthorTopics with same author and different topic
        '''
        expected_author1 = AuthorStub(["dean"],["neerav"])
        expected_topic1 = 33

        expected_author2 = AuthorStub(["dean"],["neerav"])
        expected_topic2 = 90

        author_topic1 = AuthorTopic(expected_author1, expected_topic1)
        author_topic2 = AuthorTopic(expected_author2, expected_topic2)
        
        self.assertNotEquals(author_topic1.__hash__(), author_topic2.__hash__(), "__eq__ wrongly implemented")


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
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()