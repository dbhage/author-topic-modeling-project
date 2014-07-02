'''
Created on Jul 2, 2014

@author: dbhage
'''

from author.author import get_authors
import os
from util.io import get_lines
from table.author_topic import get_author_articles
from celex.factory.factory import build_celex

dropbox_folder = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/"

# get author names
author_folder = dropbox_folder + "TopicModels/authors/"
author_files = []
lines = []

for filee in os.listdir(author_folder):
    lines += get_lines(author_folder + filee)
    
authors = get_authors(lines)
# done getting authors

articles_folder = "/home/dbhage/piperlab/JSTORAllLang&Lit1950-2008/JSTORData-09.2012/wordcounts_reduced/"
dictionary = build_celex(dropbox_folder + "celex2/", 0, 0)

aa_table = get_author_articles(articles_folder, authors, dictionary, num=1000)

with open(dropbox_folder + "TopicModels/author_articles_small_corpus_test.csv", 'w') as fd:
    for (k,v) in aa_table.items():
        fd.write(k)
        fd.write(',')
        for i in range(0, len(v)):
            fd.write(str(v[i]).replace(',', ' '))
            if i != len(v) - 1:
                fd.write(',')
        fd.write('\n')