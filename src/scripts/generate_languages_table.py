'''
Created on Oct 15, 2014

@author: dbhage

Generate language presence table for a corpus
'''

from language.detection import count_stopwords, percentage_stopwords
import os

MAIN_LANGUAGE = "english"

FOLDER_NAME = "" # path to folder containing text files on which we are to run language presence
OUTPUT_FILE = FOLDER_NAME + "/language_table.csv" # or specify your own

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

master_table = []

# for each file, get the language proportions
for filee in os.listdir(FOLDER_NAME):
    fname = FOLDER_NAME + filee
    with open(fname, 'r') as fd:
        text = fd.read()
        
    table = percentage_stopwords(count_stopwords(text))
    master_table.append((filee.replace(',', '$'), table))

# output master table
if master_table:
    with open(OUTPUT_FILE, 'w') as fd:
        # main language first in list of languages
        languages = master_table[0][1].keys()
        languages.remove(MAIN_LANGUAGE)
        languages = [MAIN_LANGUAGE] + languages
        fd.write(',' + ','.join(languages) + '\n')

        # output rows        
        for (filee, table) in master_table:
            fd.write(filee + ',' + ','.join([str(table[k]) for k in languages]) + '\n')    