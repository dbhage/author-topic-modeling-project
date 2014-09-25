'''
Created on Sep 23, 2014

@author: dbhage
'''

from mallet.parser import keys_to_csv, document_topic_matrix
from table.key import parse_keys
from table.composition import get_compositions
from util.io import get_lines

no_of_topics = 150

working_dir = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels_Novels/"

# keys
keys_file = working_dir + "keys.txt"
keys = parse_keys(get_lines(keys_file))
csv_file_name = working_dir + "keys.csv"
keys_to_csv(keys, csv_file_name)

# compositions
compositions_file = working_dir + "compositions.txt"
compositions = get_compositions(compositions_file, [])
csv_file_name = working_dir + "compositions.csv"
document_topic_matrix(compositions, no_of_topics, csv_file_name)