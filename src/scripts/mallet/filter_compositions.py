'''
Created on Sep 21, 2014

@author: dbhage

Remove foreign language topics from ORIGINAL_COMPOSITIONS_FNAME and save in COMPOSITIONS_FNAME
'''

from scripts import FOREIGN_TOPIC_REMOVE_CSV_FNAME, ORIGINAL_COMPOSITIONS_FNAME, COMPOSITIONS_FNAME
from table.composition import get_compositions, save_compositions_to_file

foreign_topics = []

with open(FOREIGN_TOPIC_REMOVE_CSV_FNAME, 'r') as fd:
    for line in fd:
        line = line.replace('\n', '')
        foreign_topics.append(int(line))

o_compositions = get_compositions(ORIGINAL_COMPOSITIONS_FNAME, foreign_topics)

save_compositions_to_file(o_compositions, COMPOSITIONS_FNAME)