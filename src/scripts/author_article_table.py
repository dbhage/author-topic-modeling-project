'''
Created on Jul 2, 2014
@author: dbhage

Script to generate author-article table in a csv file
'''

from author.author import get_authors
import os
from util.io import get_lines
from table.author_article import get_author_articles
from celex.factory.factory import build_celex
from table.author_article import save_author_articles_to_file

dropbox_folder = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/"

# get author names
author_folder = dropbox_folder + "TopicModels/authors/"
author_files = []
lines = []

for filee in os.listdir(author_folder):
    lines += get_lines(author_folder + filee)
    
authors = get_authors(lines)
# done getting authors

articles_folder = ""
dictionary = build_celex(dropbox_folder + "celex2/", 0, 0)

aa_table = get_author_articles(articles_folder, authors, dictionary)

save_author_articles_to_file(dropbox_folder + "TopicModels/author_articles_small_corpus_test.csv", aa_table)