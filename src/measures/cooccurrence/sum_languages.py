'''
Created on Sep 7, 2014

@author: dbhage
'''

from __future__ import division

def get_node_dict(lines):
    '''
    Get the node dict
    @param lines: list of strings representing lines
    @return: dict with author name as key and language as value 
    '''
    if not lines:
        raise ValueError("Lines Invalid")
    
    node_dict = {}

    for line in lines:
        if line == lines[0]: continue # first one is header row
        node = parse_node_line(line)
        node_dict[node[0]] = node[1]
    
    return node_dict

def parse_node_line(line):
    '''
    Parse a node line
    @param line: the string
    @return: 2-tuple with author name and language
    '''
    if not line:
        raise ValueError("Line invalid")
    
    line = line.replace('\n', '')
    line = line.split(',')

    return (line[0], line[2])

def get_language_sums(node_dict, edge_lines):
    '''
    @param node_dict: dict with author name as key and language as value 
    @param edge_lines: list of str list representing edge lines
    '''
    lang_sum_dict = {}
    
    for line in edge_lines:
        if line == edge_lines[0]: continue # skip header row
        edge = parse_edge_line(line) # tup(auth, auth, weight)

        for (src_auth, target_lang) in [(edge[0], node_dict[edge[1]]),(edge[1], node_dict[edge[0]])]:        

            if not src_auth in lang_sum_dict:
                lang_sum_dict[src_auth] = LanguageSum(node_dict[src_auth])
            
            if target_lang == "english":
                lang_sum_dict[src_auth].conn_eng += 1
                lang_sum_dict[src_auth].sum_eng += edge[2]
            elif target_lang == "french":
                lang_sum_dict[src_auth].conn_fre += 1
                lang_sum_dict[src_auth].sum_fre += edge[2]
            elif target_lang == "german":
                lang_sum_dict[src_auth].conn_ger += 1
                lang_sum_dict[src_auth].sum_ger += edge[2]
            else:
                raise ValueError("Language undefined:" + target_lang)
    
    return lang_sum_dict

def parse_edge_line(line):
    '''
    Parse an edge line
    @param line: the string
    @return: 3-tuple with src auth, target auth and weight
    '''
    if not line:
        raise ValueError("Line invalid")
    
    line = line.replace('\n', '')
    line = line.split(',')

    return (line[0], line[1], int(line[2]))

class LanguageSum(object):
    '''
    LanguageSum class
    '''
    
    def __init__(self, language):
        '''
        Constructor
        '''
        self.language = language
        self.sum_eng = 0
        self.sum_fre = 0
        self.sum_ger = 0
        self.conn_eng = 0
        self.conn_fre = 0
        self.conn_ger = 0
        self.english_lang_percentage = None
        self.french_lang_percentage = None
        self.german_lang_percentage = None
        self.foreign_percentage = None
    
    def calculate_language_percentages(self):
        '''
        Calculate percentage for each language
        '''
        total = self.sum_eng + self.sum_fre + self.sum_ger
        self.english_lang_percentage = self.sum_eng / total
        self.french_lang_percentage = self.sum_fre / total
        self.german_lang_percentage = self.sum_ger / total
    
    def calculate_foreign_percentage(self):
        '''
        Calculate percentage of hits which are foreign to that particular author
        '''
        total = self.sum_eng + self.sum_fre + self.sum_ger
        
        if self.language == "english":
            self.foreign_percentage = (self.sum_fre + self.sum_ger) / total
        elif self.language == "french":
            self.foreign_percentage = (self.sum_eng + self.sum_ger) / total
        elif self.language == "german":
            self.foreign_percentage = (self.sum_eng + self.sum_fre) / total
        else:
            raise Exception("Unknown language")
    
    def __str__(self):
        '''
        return LanguageSum as a string
        '''
        if not self.english_lang_percentage:
            self.calculate_language_percentages()
        
        if not self.foreign_percentage:
            self.calculate_foreign_percentage()
        
        return_string = (self.language + ','
        + str(self.sum_eng) + ',' 
        + str(self.sum_fre) + ',' 
        + str(self.sum_ger)  + ',' 
        + str(self.conn_eng) + ',' 
        + str(self.conn_fre) + ','
        + str(self.conn_ger) + ','
        + str(self.english_lang_percentage) + ','
        + str(self.french_lang_percentage) + ','
        + str(self.german_lang_percentage) + ','
        + str(self.foreign_percentage) + '\n')
        
        return return_string