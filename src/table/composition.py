'''
Created on Jun 24, 2014

@author: dbhage

Module responsible for getting compositions
'''

from util.io import get_lines
from table import PROXIMITY_THRESHOLD, TOPIC_THRESHOLD

def get_compositions(compositions_fname, topics_ignored=[]):
    '''
    Get compositions from composition_file
    
    @param compositions_fname: the path to the text file containing compositions. This file is generated by Mallet.
    @type compositions_fname: str
    
    @param topics_ignored: list of integers representing topics to be ignored
    @type topics_ignored: int list
    
    @return: dict with document name as key and Composition object as value
    @rtype: dict<str,Composition>
    '''
    lines = get_lines(compositions_fname)
    compositions = parse_compositions(lines, topics_ignored)
    return compositions

def parse_compositions(lines, topics_ignored=[]):
    '''
    Get compositions objects from a file

    @param lines: list of lines
    @type lines: str list
    
    @param topics_ignored: list of integers representing topics to be ignored
    @type topics_ignored: list of topics to be ignored when parsing compositions
    
    @return: dict with document name as key and Composition object as value
    @rtype: dict<str,Composition>
    '''
    if not lines:
        return None
    
    compositions = dict()

    for line in lines[1:]:
        composition = parse_composition(line, TOPIC_THRESHOLD, PROXIMITY_THRESHOLD)
        if line:
            # add to dict
            compositions[composition.name] = composition
        
    return compositions

def parse_composition(line, topic_threshold, proximity_threshold):
    '''
    Parse line to get one composition
    
    @param line: one composition line
    @type line: str
    
    @param topic_threshold: threshold above which a topic's proportion should be to be a main topic. Range 0-1
    @type topic_threshold: float
    
    @param proximity_threshold: a topic's proportion needs to be proximity_threshold % of the main topic's proportion to be considered too. Range 0-1
    @type proximity_threshold: float
    
    @return: composition obj
    @rtype: Composition
    '''
    if not line:
        raise ValueError("Line invalid")
    
    if topic_threshold <= 0 or topic_threshold > 1:
        raise ValueError("Topic Threshold out of range")
    
    if proximity_threshold <= 0 or proximity_threshold > 1:
        raise ValueError("Proximity Threshold out of range")
        
    composition = Composition()
    
    split_line = line.split()
    
    # get document data
    composition.doc_no = int(split_line[0])
    composition.name = split_line[1].split('/')[-1]

    # add main topic to composition
    try:
        main_topic = int(split_line[2])
        main_topic_proportion = float(split_line[3])
    except IndexError:
        return composition
    
    if main_topic_proportion < topic_threshold:
        return composition
    
    composition.main_topic = main_topic
    composition.main_topics.append(main_topic)
    composition.add_topic_proportion(main_topic, main_topic_proportion)

    # find other topics close enough to main topic    
    count = 4
    while count < len(split_line) - 1:

        topic = int(split_line[count])
        proportion = float(split_line[count + 1])
        
        if proportion > topic_threshold and proportion >= proximity_threshold * main_topic_proportion:
            # within proximity_threshold% of top topic, so add as a main topic
            composition.main_topics.append(topic)
            composition.add_topic_proportion(topic, proportion)
            count += 2
        else:
            break
    
    return composition

def save_compositions_to_file(compositions, txt_file_name):
    '''
    Save a list of compositions to a text file
    
    @param compositions: list of Compositions
    @type compositions: Composition list
    
    @param txt_file_name: text for file name
    @type txt_file_name: str
    '''
    with open(txt_file_name, 'w') as fd:
        fd.write("#doc name topic proportion ...\n")
        for (a_name, composition) in compositions.items():
            fd.write(str(composition.doc_no) + '\t')
            fd.write(a_name + '\t')
            for main_topic in composition.main_topics:
                fd.write(str(main_topic) + ' ' + str(composition.topic_proportions[main_topic]) + ' ')
            fd.write('\n')

class Composition(object):
    '''
    @summary: Data Structure to represent a composition for a document. 
    '''
    def __init__(self):
        '''
        Constructor
        
        @postcondition: members doc_no, name, topic_proportions, main_topic, main_topics have been created
        '''
        self.doc_no = -1
        self.name = ''
        self.topic_proportions = dict()
        self.main_topic = None
        self.main_topics = []
        
    def add_topic_proportion(self, topic, proportion):
        '''
        Add a topic number and its proportion
        
        @param topic: topic number
        @type topic: int
        
        @param proportion: the proportion of the text which is related to this topic
        @type proportion: float
        
        @precondition: self.topic_proportions must have been initialised with an empty dict
        
        @postcondition: self.topic_proportions now has (topic, proportion) key-value pair
        '''
        self.topic_proportions[topic] = proportion
        
    def __str__(self):
        return str(self.doc_no) + " " + self.name + " " + str(self.topic_proportions)