'''
Created on Oct 13, 2014

@author: dbhage
'''

from author.galenet import name_split_re, re

def get_name_list(text):
    names = re.split(name_split_re, text)
    return [name for name in names if len(name) > 1]                