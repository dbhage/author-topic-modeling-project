'''
Created on Jun 24, 2014

@author: dbhage
'''

def parse_keys(lines):
    '''
    Get keys objects from a file
    @param lines: array of strings representing the lines from a keys file generated by mallet
    '''
    keys = []
    
    for line in lines:
        key = Key()
        split_line = line.split()
        
        key.topic_no = int(split_line[0])
        key.dirichlet_no = float(split_line[1])
        
        counter = 2
        
        while counter < len(split_line):
            key.add_word(split_line[counter])
            counter += 1
        
        keys.append(key)
    
    return keys        

class Key(object):
    '''
    Data structure to represent a key (topic)
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.topic_no = -1
        self.dirichlet_no = -1
        self.words = []
        
    def add_word(self, word):
        self.words.append(word)
    
    def add_words(self, words):
        self.words += words
    
    def __str__(self):
        return str(self.topic_no) + " " + str(self.dirichlet_no) + " " + str(self.words)