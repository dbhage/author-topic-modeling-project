'''
Created on Aug 14, 2014

@author: dbhage
'''

from table.composition import get_compositions
import sys
from corpus.jstor.citations_parser import get_citations
from util.io import get_lines

print ("Starting")

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 4/compositions.txt"
compositions = get_compositions(compositions_file)

citations_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/citations.CSV"
citations = get_citations(get_lines(citations_file))
citations_dict = dict()

for citation in citations:
    new_id = "wordcounts_" + citation.id.replace('/', '_') + ".txt"
    if new_id in citations_dict:
        raise Exception(new_id + " should not be in dict")
    else:
        citations_dict[new_id] = citation
        
if compositions:
    with open("/home/dbhage/piperlab/pubdate_topic.csv", 'w') as fd:
        fd.write("pub date,main topic\n")
        for (a_name, composition) in compositions.items():
            fd.write(str(citations_dict[a_name].pub_date) + ',' + str(composition.main_topic) + '\n')
else:
    print >> sys.stderr, "Compositions None"

print ("Done.")