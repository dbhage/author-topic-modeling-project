'''
Created on Oct 13, 2014

@author: dbhage

Parse author names from lines from author file obtained from galenet data
'''

from names import get_name_list
from author.author import Author
from util.string import get_longest_string

def get_authors(lines):
    '''
    Get author objects
    @param lines: lines from file
    @return: list of Author objects
    '''
    authors = []
    
    for line in lines:
        author = get_author(line)
        if author:
            if not author.last_names or not author.first_names:
                # we only want author names with at least 1 first and last name
                continue
            
            if len(author.last_names) > 1:
                author.last_names = [get_longest_string(author.last_names)]
            
            authors.append(author)
    
    return authors

def get_author(line):
    '''
    Get author object
    @param line: line representing author full name
    @return Author object
    '''
    author = Author()
    names = line.split(',')

    # get last name(s)
    last_names = get_name_list(names[0])
    if last_names:
        author.add_last_names(last_names)
    
    # get first name(s) if any
    if len(names) > 1:
        first_names = get_name_list(names[1])
        if first_names:
            author.add_first_names(first_names)
        
    return author