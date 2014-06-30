'''
Created on Jun 25, 2014

@author: dbhage

Module to extract author names from text.
'''

import re

def extract_author_names(text):
    '''
    Extract author names from text
    @param text: string from which to extract names
    @return: list of strings with the names found, [] if no names found
    '''
    if text:
        text = re.sub(r"Mrs\.|Mr\.", '', text)
        
        name = find_dot_pattern(text)
        if name:
            return name
    
        return find_upper_lowers_pattern(text)
    return []

def find_dot_pattern(text):
    '''
    Find initials.
    @param text: the text in which to find the initials
    @return: list of strings with the names found, [] if no names found
    '''
    if text:
        if '.' in text:
            if re.match(r"([A-Z]\.){2,}", text):
                return [re.sub(r"\s+", '', text)]
    return []

def find_upper_lowers_pattern(text):
    '''
    Find names starting with an upper case lette followed by lower case letters
    @param text: the text in which to find the pattern
    @return: list of strings with the names found, [] if no names found
    '''
    if text:
        return re.findall(r"[A-Z][a-z]+", text)
    return []