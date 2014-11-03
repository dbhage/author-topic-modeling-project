'''
Created on Sep 7, 2014

@author: dbhage
'''

from measures.cooccurrence.sum_languages import get_node_dict, get_language_sums
from util.io import get_lines
from scripts import SUM_AND_CONNECTIONS_OUTPUT_FNAME, NODE_FNAME, AUTHOR_COOCCURRENCE_EDGE_LIST_PLUS10 as EDGE_FNAME
import time

print ("Starting:" + str(time.clock()))

lines = get_lines(NODE_FNAME)

node_dict = get_node_dict(lines)

lines = get_lines(EDGE_FNAME)

lang_sums = get_language_sums(node_dict, lines)

with open(SUM_AND_CONNECTIONS_OUTPUT_FNAME, 'w') as fd:
    fd.write("auth,lang,sum_eng,sum_fre,sum_ger,conn_eng,conn_fre,conn_ger,english language percentage,french language percentage,german language percentage,foreign percentage\n")
    for (auth, lang_sum) in lang_sums.items():
        fd.write(auth + ',' + str(lang_sum))

print ("Done:" + str(time.clock()))