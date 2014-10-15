'''
Created on Jul 10, 2014

@author: dbhage

Module to parse citations file in Citation objects

'''

from datetime import date
import re

def get_citations(lines):
    '''
    Get citations list
    @param lines: lines from citations csv file
    @return: list of Citation objects
    '''
    if lines is None or lines == []:
        return []

    citations = []
    
    for line in lines:
        citation = Citation()
        citation = get_citation(line, citation)
        if citation:
            citations.append(citation)

    return citations

def get_citation(line, citation):
    if line is None or line == '' or citation is None:
        return None
    
    line = line.replace('\n', '')
    
    try:
        citation_data = line.split('\t')
        citation.id = citation_data[0]
        citation.doi = citation_data[1]
        citation.title = citation_data[2]
        citation.author = citation_data[3]
        citation.journal_title = citation_data[4]
        citation.issue = citation_data[6]
        citation.set_pub_date(citation_data[7])
        citation.page_range = citation_data[8]
        citation.publisher = citation_data[9]
        citation.type = citation_data[10]
        return citation
    except IndexError:
        return None

class Citation(object):
    '''
    Citation class
    '''
    def __init__(self):
        '''
        Initialise members
        '''        
        self.id = ""
        self.doi = ""
        self.title = ""
        self.author = ""
        self.journal_title = ""
        self.volume = -1
        self.issue = ""
        self.pub_date = None
        self.page_range = ""
        self.publisher = ""
        self.type = ""
        self.reviewed_work = ""
    
    def set_pub_date(self, date_str):
        '''
        Set the publication date using a string
        @param date_str: the string containing the date in YYYY-MM-DD format.
        @precondition: self.pub_date must exist
        '''
        if date_str:
            date_str = re.search(r"[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2}", date_str)
            if date_str:
                date_str = date_str.group(0)
                date_str = date_str.split('-')
                self.pub_date = date(int(date_str[0]), int(date_str[1]), int(date_str[2]))