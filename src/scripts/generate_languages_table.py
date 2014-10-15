'''
Created on Oct 15, 2014

@author: dbhage

Generate language presence table for a corpus
'''

from language.detection import count_stopwords, percentage_stopwords
import os

MAIN_LANGUAGE = "english"

FOLDER_NAME = "/home/dbhage/piperlab/language_test/"
OUTPUT_FILE = "/home/dbhage/piperlab/language_test/language_table.csv"

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

master_table = []

for filee in os.listdir(FOLDER_NAME):
    fname = FOLDER_NAME + filee
    with open(fname, 'r') as fd:
        text = fd.read()
        
    table = percentage_stopwords(count_stopwords(text))
    master_table.append((filee.replace(',', '$'), table))

if master_table:
    with open(OUTPUT_FILE, 'w') as fd:
        languages = master_table[0][1].keys()
        languages.remove(MAIN_LANGUAGE)
        languages = [MAIN_LANGUAGE] + languages
        fd.write(',' + ','.join(languages) + '\n')
        for (filee, table) in master_table:
            fd.write(filee + ',' + ','.join([str(table[k]) for k in languages]) + '\n')    