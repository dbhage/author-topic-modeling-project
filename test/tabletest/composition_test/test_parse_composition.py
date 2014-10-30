'''
Created on Oct 30, 2014 (Happy birthday to me!)

@author: dbhage

Module to test table.composition.parse_composition(...)
'''

import unittest
from table.composition import parse_composition

class TestParseComposition(unittest.TestCase):
    '''
    test class to test parse_composition function
    '''
    def test_case1(self):
        '''
        TC1: line empty 
        '''
        line = ""
        topic_threshold = .1
        proximity_threshold = .9
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case2(self):
        '''
        TC2: line None 
        '''
        line = None
        topic_threshold = .1
        proximity_threshold = .9
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case3(self):
        '''
        TC3: boundary invalid case. topic_threshold <= 0 
        '''
        line = "bcejksbc jks"
        topic_threshold = 0
        proximity_threshold = .9
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case4(self):
        '''
        TC4: invalid case. topic_threshold <= 0 
        '''
        line = "bcejksbc jks"
        topic_threshold = -3
        proximity_threshold = .9
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case5(self):
        '''
        TC5: invalid case. topic_threshold > 1 
        '''
        line = "bcejksbc jks"
        topic_threshold = 1.1
        proximity_threshold = .9
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case6(self):
        '''
        TC6: boundary invalid case. proximity_threshold <= 0 
        '''
        line = "bcejksbc jks"
        topic_threshold = .9
        proximity_threshold = 0
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case7(self):
        '''
        TC7: invalid case. proximity_threshold <= 0 
        '''
        line = "bcejksbc jks"
        topic_threshold = .9
        proximity_threshold = -3
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case8(self):
        '''
        TC8: invalid case. proximity_threshold > 1 
        '''
        line = "bcejksbc jks"
        topic_threshold = .9
        proximity_threshold = 1.1
        self.assertRaises(ValueError, parse_composition, line, topic_threshold, proximity_threshold)

    def test_case9(self):
        '''
        TC9: valid case. No topics found
        '''
        line = "1    file1   142    0.17184653916211293    188    0.12471539162112934    218    0.10900500910746813    219    0.06563069216757741"
        topic_threshold = .2
        proximity_threshold = .9
        actual_composition = parse_composition(line, topic_threshold, proximity_threshold)

        expected_doc_no = 1
        expected_name = "file1"
        expected_topic_proportions = {}
        expected_main_topic = None
        expected_main_topics = []

        composition_equality = composition_equal(actual_composition, expected_doc_no, expected_name, expected_topic_proportions, expected_main_topic, expected_main_topics)
        
        self.assertTrue(composition_equality)

    def test_case10(self):
        '''
        TC10: valid case. 1 topic found
        '''
        line = "1    file1   142    0.17184653916211293    188    0.12471539162112934    218    0.10900500910746813    219    0.06563069216757741"
        topic_threshold = .15
        proximity_threshold = .9
        actual_composition = parse_composition(line, topic_threshold, proximity_threshold)

        expected_doc_no = 1
        expected_name = "file1"
        expected_topic_proportions = {142: 0.17184653916211293}
        expected_main_topic = 142
        expected_main_topics = [142]

        composition_equality = composition_equal(actual_composition, expected_doc_no, expected_name, expected_topic_proportions, expected_main_topic, expected_main_topics)
        
        self.assertTrue(composition_equality)

    def test_case11(self):
        '''
        TC11: valid case. 2 topics found
        '''
        line = "1    file1   142    0.17184653916211293    188    0.12471539162112934    218    0.10900500910746813    219    0.06563069216757741"
        topic_threshold = .12
        proximity_threshold = .7
        actual_composition = parse_composition(line, topic_threshold, proximity_threshold)

        expected_doc_no = 1
        expected_name = "file1"
        expected_topic_proportions = {142: 0.17184653916211293, 188: 0.12471539162112934}
        expected_main_topic = 142
        expected_main_topics = [142, 188]

        composition_equality = composition_equal(actual_composition, expected_doc_no, expected_name, expected_topic_proportions, expected_main_topic, expected_main_topics)
        
        self.assertTrue(composition_equality)

    def test_case12(self):
        '''
        TC12: valid case. 3 topics found
        '''
        line = "1    file1   142    0.17184653916211293    188    0.12471539162112934    218    0.10900500910746813    219    0.06563069216757741"
        topic_threshold = .1
        proximity_threshold = .5
        actual_composition = parse_composition(line, topic_threshold, proximity_threshold)

        expected_doc_no = 1
        expected_name = "file1"
        expected_topic_proportions = {142: 0.17184653916211293, 188: 0.12471539162112934, 218: 0.10900500910746813}
        expected_main_topic = 142
        expected_main_topics = [142, 188, 218]

        composition_equality = composition_equal(actual_composition, expected_doc_no, expected_name, expected_topic_proportions, expected_main_topic, expected_main_topics)
        
        self.assertTrue(composition_equality)

def composition_equal(actual_composition, expected_doc_no, expected_name, expected_topic_proportions, expected_main_topic, expected_main_topics):
    '''
    Check if composition's members equal to expected values.
    
    @param actual_composition: the composition obj which we are checking
    @type actual_composition: Composition
    
    @param expected_doc_no: expected document number
    @type expected_doc_no: int
    
    @param expected_name: expected name
    @type expected_name: str
    
    @param expected_topic_proportions: expected topic proportions
    @type expected_topic_proportions: dict<int, float>
    
    @param expected_main_topic: expected main topic 
    @type expected_main_topic: int
    
    @param expected_main_topics: list of expected main topics
    @type expected_main_topics: int list
    
    @return: true if actual composition and expected values match
    @rtype: bool
    '''
    doc_no_equals = actual_composition.doc_no == expected_doc_no
    name_equals = actual_composition.name == expected_name
    topic_proportions_equals = actual_composition.topic_proportions == expected_topic_proportions
    main_topic_equals = actual_composition.main_topic == expected_main_topic
    main_topics_equals = actual_composition.main_topics == expected_main_topics
    return doc_no_equals and name_equals and topic_proportions_equals and main_topic_equals and main_topics_equals
    
if __name__ == "__main__":
    unittest.main()