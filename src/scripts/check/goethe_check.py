'''
Created on Oct 16, 2014

@author: dbhage

Check some values for Goethe only.
'''

from measures.cooccurrence.sum_languages import get_node_dict
from util.io import get_lines
from scripts import NODE_FNAME, EDGE_FNAME
import time

print ("Starting:" + str(time.clock()))

lines = get_lines(NODE_FNAME)
node_dict = get_node_dict(lines)
lines = get_lines(EDGE_FNAME)

goethe = "johann goethe"

counts = 0
weight_sums = 0
german_author_set = set()

for i,line in enumerate(lines):

    if i==0 or goethe not in line: continue
    
    line = line.replace('\n', '')
    line = line.split(',')

    auth1 = line[0]
    auth2 = line[1]
    weight = int(line[2])
    
    if goethe == auth1:
        other = auth2
    elif goethe == auth2:
        other = auth1
    else:
        raise Exception("wat da")
    
    if node_dict[other] == "german":
        counts += 1
        weight_sums += weight
        german_author_set.add(other)

print (counts)
print (weight_sums)
print (len(german_author_set))
print (german_author_set)