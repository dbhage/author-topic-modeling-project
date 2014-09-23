'''
Created on Sep 21, 2014

@author: dbhage

Remove foreign language topics from original_compositions and save in compositions_file
'''

from scripts import foreign_topic_remove_csv, original_compositions, compositions_file
from table.composition import get_compositions, save_compositions_to_file

foreign_topics = []

with open(foreign_topic_remove_csv, 'r') as fd:
    for line in fd:
        line = line.replace('\n', '')
        foreign_topics.append(int(line))

o_compositions = get_compositions(original_compositions, foreign_topics)

save_compositions_to_file(o_compositions, compositions_file)