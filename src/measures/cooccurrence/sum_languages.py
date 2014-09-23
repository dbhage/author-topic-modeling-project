'''
Created on Sep 7, 2014

@author: dbhage
'''

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
                lang_sum_dict[src_auth] = LanguageSum()
            
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
    def __init__(self):
        self.sum_eng = 0
        self.sum_fre = 0
        self.sum_ger = 0
        self.conn_eng = 0
        self.conn_fre = 0
        self.conn_ger = 0
    
    def __str__(self):
        return str(self.sum_eng) + ',' + str(self.sum_fre) + ',' + str(self.sum_ger)  + ',' + str(self.conn_eng) + ',' + str(self.conn_fre) + ',' + str(self.conn_ger) + '\n'