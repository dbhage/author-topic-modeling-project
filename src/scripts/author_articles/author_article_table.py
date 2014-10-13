'''
Created on Jul 2, 2014

@author: dbhage

Script to generate author-article table in a csv file
'''

import author
from util.io import get_lines
from table.author_article import get_author_articles, save_author_articles_to_file
from scripts import AUTHOR_NODE_LIST_FOLDER, AUTHOR_ARTICLE_CSV_FNAME, GALENET_AUTHOR_MASTER_LIST_FNAME
import os, time

GALENET = True # True if we are using galenet author list

# import function based on author list
if not GALENET:
    from author.author import get_authors
else:
    from author.galenet.author_name_parser import get_authors

BIGRAMS = True # are we using bigrams data or unigrams?

author_files = []
lines = []

print ("Starting:" + str(time.clock()))

# get lines which contain author names
if not GALENET:
    for filee in os.listdir(AUTHOR_NODE_LIST_FOLDER):
        lines += get_lines(AUTHOR_NODE_LIST_FOLDER + filee)
else:
    # use galenet
    lines = get_lines(GALENET_AUTHOR_MASTER_LIST_FNAME)

# parse lines and get author names
authors = get_authors(lines)

# folder where articles are found
articles_folder = "ARTICLES FOLDER PATH"

# list of authors for which we can only use last names
last_name_only_list = "goethe balzac proust woolf dickens melville poe diderot flaubert verne stendhal zola fontane hoelderlin kafka novalis rilke schiller wieland"

# get author article table
aa_table = get_author_articles(articles_folder, authors, last_name_only_list.split(' '), BIGRAMS)

# save author articles to file
save_author_articles_to_file(AUTHOR_ARTICLE_CSV_FNAME, aa_table)

print ("Done:" + str(time.clock()))