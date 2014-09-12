'''
Created on Jul 2, 2014

@author: dbhage

Script to generate author-article table in a csv file
'''

from author.author import get_authors
import os, time
from util.io import get_lines
from table.author_article import get_author_articles
from table.author_article import save_author_articles_to_file

dropbox_folder = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/"
bigrams = True # are we using bigrams data or unigrams?
author_folder = dropbox_folder + "TopicModels/authors/list/"
author_files = []
lines = []

print ("Starting:" + str(time.clock()))

for filee in os.listdir(author_folder):
    lines += get_lines(author_folder + filee)
    
authors = get_authors(lines)

articles_folder = dropbox_folder + "TopicModels/bigrams_data_sample/"

last_name_only_list = "goethe balzac proust woolf dickens melville poe diderot flaubert verne stendhal zola fontane hoelderlin kafka novalis rilke schiller wieland"

aa_table = get_author_articles(articles_folder, authors, last_name_only_list.split(' '), bigrams)

if not bigrams:
    saved_file_name = dropbox_folder + "TopicModels/Trial 5 - Bigrams/author_articles_small_corpus.csv"
else:
    saved_file_name = dropbox_folder + "TopicModels/Trial 5 - Bigrams/author_articles_small_corpus_using_bigrams.csv"
    
save_author_articles_to_file(saved_file_name, aa_table)

print ("Done:" + str(time.clock()))