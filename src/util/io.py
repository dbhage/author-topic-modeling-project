'''
Created on Jun 24, 2014

@author: dbhage

IO utility functions
'''

import sys

def get_lines(fname):
    '''
    Get lines as a string list
    @param fname: file name
    @return: list of string
    '''
    try:
        with open(fname, 'r') as fd:
            content = fd.readlines()
            return content
    except IOError:
        print >> sys.stderr, "IO Error when opening " + fname
        return None