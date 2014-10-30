'''
Created on Aug 14, 2014

@author: dbhage

Script to generate a table of publication dates and topics
'''

from table.composition import get_compositions
import sys, time
from corpus.jstor.citations_parser import get_citations
from util.io import get_lines
from scripts import COMPOSITIONS_FNAME, CITATIONS_FILE_FNAME, PUBDATE_TOPIC_CSV_FNAME

print ("Starting:" + str(time.clock()))

compositions = get_compositions(COMPOSITIONS_FNAME)

citations = get_citations(get_lines(CITATIONS_FILE_FNAME))
citations_dict = dict()

for citation in citations:
    new_id = "bigrams_" + citation.id.replace('/', '_') + ".txt"
    citations_dict[new_id] = citation
        
if compositions:
    with open(PUBDATE_TOPIC_CSV_FNAME, 'w') as fd:
        fd.write("pub date,main topic\n")
        for (a_name, composition) in compositions.items():
            for main_topic in composition.main_topics:
                fd.write(str(citations_dict[a_name].pub_date) + ',' + str(main_topic) + '\n')
else:
    print >> sys.stderr, "Compositions None"

print ("Done:" + str(time.clock()))