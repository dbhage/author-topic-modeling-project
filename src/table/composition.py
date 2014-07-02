'''
Created on Jun 24, 2014

@author: dbhage
'''

from util.io import get_lines

def get_compositions(compositions_file):
    '''
    Get compositions from composition_file
    @param compositions_file: the path to the text file containing compositions. This file is generated by Mallet.
    @return: dict with document name as key and Composition object as value
    '''
    lines = get_lines(compositions_file)
    compositions = parse_compositions(lines)
    return compositions

def parse_compositions(lines):
    '''
    Get compositions objects from a file
    @return: dict with document name as key and Composition object as value
    '''
    compositions = dict()

    for line in lines[1:]:
        composition = Composition()
        split_line = line.split()
        composition.doc_no = int(split_line[0])
        composition.name = split_line[1].split('/')[-1]
        # get topic proportions
        counter = 2
        main_topic = (-1, 0)
        
        while counter < len(split_line):
            topic = int(split_line[counter])
            proportion = float(split_line[counter + 1])
            composition.add_topic_proportion(topic, proportion)
            
            if proportion > main_topic[1]:
                main_topic = (topic, proportion) 
            
            counter += 2
        
        composition.main_topic = main_topic[0]
        compositions[composition.name] = composition
        
    return compositions

class Composition(object):
    '''
    Data Structure to represent a composition for a document. 
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.doc_no = -1
        self.name = ''
        self.topic_proportions = dict()
        self.main_topic = None
        
    def add_topic_proportion(self, topic, proportion):
        '''
        @precondition: self.topic_proportions must have been initialised with an empty dict
        '''
        self.topic_proportions[topic] = proportion
        
    def __str__(self):
        return str(self.doc_no) + " " + self.name + " " + str(self.topic_proportions)