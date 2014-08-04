'''
Created on Aug 3, 2014

@author: dbhage
'''

import unittest

from measures.entropy import entropy_summation

class TestEntropySummation(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Valid case. 1 iteration only.
        '''
        auth = AuthorStub(["dean"], ["neerav"])
        topic_list = [1]
        author_topic_counts = {AuthorTopicStub(auth, 1):5}
        n = 10
        
        actual = entropy_summation(auth, topic_list, author_topic_counts, n, formula_inside_sum_stub)
        expected = -0.34657359028

        self.assertAlmostEquals(actual, expected, 10, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case2(self):
        '''
        TC2: Valid case. 2 iterations.
        '''
        auth = AuthorStub(["dean"], ["neerav"])
        topic_list = [1,2]
        author_topic_counts = {AuthorTopicStub(auth, 1):5,
                               AuthorTopicStub(auth, 2):50,
                               AuthorTopicStub(AuthorStub([], []), 8):23}

        n = 55
        
        actual = entropy_summation(auth, topic_list, author_topic_counts, n, formula_inside_sum_stub)
        expected = -0.30463609734

        self.assertAlmostEquals(actual, expected, 10, "Expected: " + str(expected) + " Actual: " + str(actual))

def formula_inside_sum_stub(nh, n):
    '''
    STUB for measures.entropy.formula_inside_sum
    @param nh: number of documents with that topic, containing that author
    @param n: total number of documents for that author
    '''
    if nh == 5 and n == 10:
        return -0.34657359028
    if nh == 5 and n == 55:
        return -0.21799047934
    if nh == 50 and n == 55:
        return -0.086645618

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

class AuthorTopicStub(object):

    def __init__(self, names, topic):
        self.author = names
        self.topic = topic
    
    def __eq__(self, other):
        return self.author == other.author and self.topic == other.topic
    
    def __str__(self):
        return "Author:" + str(self.author) + " Topic: " + str(self.topic)

    def __hash__(self):
        return hash((self.author, self.topic))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()