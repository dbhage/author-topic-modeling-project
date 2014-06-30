'''
Created on Jun 24, 2014

@author: dbhage
'''

import sys

def get_lines(fname):
    try:
        with open(fname, 'r') as fd:
            content = fd.readlines()
            return content
    except IOError:
        print >> sys.stderr, "IO Error when opening " + fname
        return None