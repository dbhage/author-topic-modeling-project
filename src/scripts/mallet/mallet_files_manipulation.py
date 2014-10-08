'''
Created on Sep 23, 2014

@author: dbhage

Script for parsing keys and compositions file.
'''

from mallet.parser import keys_to_csv1, document_topic_matrix
from table.key import parse_keys
from table.composition import get_compositions
from util.io import get_lines

# number of topics
no_of_topics = 150

# specify working directory where keys and compositions files generated from mallet are found
working_dir = "WORKING DIRECTORY"

# parse keys
keys_file = working_dir + "keys.txt"
keys = parse_keys(get_lines(keys_file))
csv_file_name = working_dir + "keys.csv"
keys_to_csv1(keys, csv_file_name)

# parse compositions
compositions_file = working_dir + "compositions.txt"
compositions = get_compositions(compositions_file, [])
csv_file_name = working_dir + "compositions.csv"
document_topic_matrix(compositions, no_of_topics, csv_file_name)