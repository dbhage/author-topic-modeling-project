'''
Created on Aug 14, 2014

@author: dbhage
'''

from table.composition import get_compositions
import sys, time
from corpus.jstor.citations_parser import get_citations
from util.io import get_lines
from scripts import compositions_file, citations_file, pubdate_topic_csv_file

print ("Starting:" + str(time.clock()))

compositions = get_compositions(compositions_file)

citations = get_citations(get_lines(citations_file))
citations_dict = dict()

for citation in citations:
    new_id = "bigrams_" + citation.id.replace('/', '_') + ".txt"
    citations_dict[new_id] = citation
        
if compositions:
    with open(pubdate_topic_csv_file, 'w') as fd:
        fd.write("pub date,main topic\n")
        for (a_name, composition) in compositions.items():
            fd.write(str(citations_dict[a_name].pub_date) + ',' + str(composition.main_topic) + '\n')
else:
    print >> sys.stderr, "Compositions None"

print ("Done:" + str(time.clock()))