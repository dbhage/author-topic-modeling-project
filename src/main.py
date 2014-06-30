'''
Created on Jun 24, 2014

@author: dbhage
'''

from mallet.mallet import import_data, train
from util.io import get_lines
from parser.composition import parse_compositions
from parser.key import parse_keys
from parser.author_article import find_authors
from author.author import get_authors
from celex.factory.factory import build_celex

import os

# Import Data
data_folder = ""
mallet_folder = "/home/dbhage/mallet/mallet/"
mallet_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/" + "topic-input-smallcorpus-nsw.mallet"

#import_data(mallet_folder, data_folder, mallet_file)

# Topic model
main_folder = "/home/dbhage/piperlab/TopicModeling/"
compositions_file = main_folder + "compositions.txt"
keys_file = main_folder + "keys.txt"
no_of_topics = 300

#train(mallet_folder, mallet_file, no_of_topics, keys_file, compositions_file)

# parse compositions & keys    
#compositions = parse_compositions(get_lines(compositions_file))
#keys = parse_keys(get_lines(keys_file))

# get authors
lines = []
author_files = ["/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/authors/Novel_Authors_English.csv", 
                "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/authors/Novel_Authors_French.csv",
                "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/authors/Novel_Authors_German.csv"]

for af in author_files:
    lines += get_lines(af)

authors = get_authors(lines)

# produce author article table
articles_folder = "/home/dbhage/piperlab/JSTORAllLang&Lit1950-2008/JSTORData-09.2012/wordcounts_reduced/"

lines = []

celex = build_celex("/home/dbhage/Dropbox/PiperLabDeanSharedFolder/celex2/", 0, 0)

for article in sorted(os.listdir(articles_folder))[:100]:
    
    article_content = open(articles_folder + article).read()
    auths = find_authors(authors, article_content, celex)

    current_line = article + ','
    
    for auth in auths:
        current_line += str(auth) + ','
    
    current_line = current_line[:len(current_line)-1]
    
    lines.append(current_line)

with open("/home/dbhage/piperlab/author_article_table.csv", 'w') as fd:
    for line in lines:
        fd.write(line + '\n')