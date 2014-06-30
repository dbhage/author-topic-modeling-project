'''

Created on Jun 25, 2014

@author: dbhage

'''

from names import extract_author_names
from util.string import to_lower

def get_authors(lines):
    '''
    Get author objects
    @param lines: string with names separated by commas or spaces
    @return: list of author objects extracted from lines
    '''
    authors = []
    
    if lines:

        for line in lines:
            
            names = line.replace('\n', '')
            names = names.split(',')
                
            author = Author()
                
            for i in range(0, len(names)):
                
                name_list = extract_author_names(names[i])
                
                if i == 0:
                    author.add_last_names(name_list)
                else:
                    author.add_first_names(name_list)
                
            authors.append(author)

    return authors

class Author(object):
    
    def __init__(self):
        self.first_names = []
        self.last_names = []
    
    def add_first_name(self, first_name):
        if first_name:
            self.first_names.append(first_name.lower())
    
    def add_last_name(self, last_name):
        if last_name:
            self.last_names.append(last_name.lower())

    def add_first_names(self, first_names):
        if first_names:
            self.first_names += map(to_lower, first_names)
    
    def add_last_names(self, last_names):
        if last_names:
            self.last_names += map(to_lower, last_names)
    
    def __str__(self):
        return  ' '.join(self.last_names) + ", " + ' '.join(self.first_names)
    
    def __eq__(self, other):
        return other.first_names == self.first_names and other.last_names == self.last_names