'''
Created on Sep 7, 2014

@author: dbhage
'''

from measures.cooccurrence.sum_languages import get_node_dict, get_language_sums
from util.io import get_lines
from scripts import sum_and_connections_output_file, node_file, edge_file
import time

print ("Starting:" + str(time.clock()))

lines = get_lines(node_file)

node_dict = get_node_dict(lines)

lines = get_lines(edge_file)

lang_sums = get_language_sums(node_dict, lines)

with open(sum_and_connections_output_file, 'w') as fd:
    fd.write("auth,lang,sum_eng,sum_fre,sum_ger,conn_eng,conn_fre,conn_ger,english language percentage,french language percentage,german language percentage,foreign percentage\n")
    for (auth, lang_sum) in lang_sums.items():
        fd.write(auth + ',' + str(lang_sum))

print ("Done:" + str(time.clock()))