'''
Created on Sep 7, 2014

@author: dbhage
'''

from measures.cooccurrence.sum_languages import get_node_dict, get_language_sums
from util.io import get_lines

import time

print ("Starting:" + str(time.clock()))

main_dir = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 5 - Bigrams/1950-1980/"

node_file = main_dir + "Author_Cooccurrence_Nodelist_1950_1980.csv"
lines = get_lines(node_file)
node_dict = get_node_dict(lines)

edge_file = main_dir + "Author_Cooccurrence_Edgelist_Top5_1950_1980.csv"
lines = get_lines(edge_file)

lang_sums = get_language_sums(node_dict, lines)

output_file = main_dir + "sum_and_connections.csv"

with open(output_file, 'w') as fd:
    fd.write("auth,sum_eng,sum_fre,sum_ger,conn_eng,conn_fre,conn_ger\n")
    for (auth, lang_sum) in lang_sums.items():
        fd.write(auth + ',' + str(lang_sum))

print ("Done:" + str(time.clock()))