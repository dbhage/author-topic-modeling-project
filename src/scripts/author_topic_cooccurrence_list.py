'''
Created on Sep 21, 2014

@author: dbhage
@precondition: author topic table must already have been generated (by running author_topic_table.py script)
'''

from scripts import AUTHOR_TOPIC_COOCCURRENCE_LIST_FNAME, AUTHOR_TOPIC_CSV_FNAME

topic_authors_dict = {} # dict<topic,auth>

with open(AUTHOR_TOPIC_CSV_FNAME, 'r') as fd:
    lines = fd.readlines()
    for i in range(0, len(lines)):
        if i==0: continue
        
        line = lines[i].replace('\n', '')
        line = line.split(',')
        
        if line[0] not in topic_authors_dict:
            topic_authors_dict[line[0]] = set()

        topic_authors_dict[line[0]].add(line[1])

with open(AUTHOR_TOPIC_COOCCURRENCE_LIST_FNAME, 'w') as fd:        
    fd.write("auth1,auth2,shared topic\n")
    for (topic, auths) in topic_authors_dict.items():
        auths = list(auths)
        for i in range(0, len(auths)):
            for j in range(i+1, len(auths)):
                fd.write(auths[i] + ',' + auths[j] + ',' + topic + '\n')

print ("Done")