'''
Created on Oct 15, 2014

@author: dbhage

Generate language presence table for a corpus
'''

from language.detection import count_stopwords, percentage_stopwords
import os
from nltk.corpus import stopwords
from scripts import DROPBOX_FOLDER, ARTICLES_FOLDER
from util.io import get_lines

MAIN_LANGUAGE = "english"

FOLDER_NAME = ARTICLES_FOLDER # path to folder containing text files on which we are to run language presence
OUTPUT_FILE = DROPBOX_FOLDER + "TopicModels/language_table_all.csv" # or specify your own

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

master_table = []

# get stopwords
stopwords_dict = {}
for language in stopwords.fileids():
    stopwords_set = set(stopwords.words(language))
    stopwords_dict[language] = stopwords_set

stopwords_folder = DROPBOX_FOLDER + "TopicModels/stopwords/"
additional_stopword_files = {"japanese": "stopwords-japanese.txt", "chinese": "stopwords-chinese.txt"}

for (language, filee) in additional_stopword_files.items():
    lines = get_lines(stopwords_folder + filee)
    lines = map(lambda x:x.replace('\n', ''), lines)
    words = set(lines)
    stopwords_dict[language] = words

# for each file, get the language proportions
for filee in os.listdir(FOLDER_NAME):
    print (filee)
    fname = FOLDER_NAME + filee
    
    with open(fname, 'r') as fd:
        text = fd.read()
        
    table = percentage_stopwords(count_stopwords(text, stopwords_dict))
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