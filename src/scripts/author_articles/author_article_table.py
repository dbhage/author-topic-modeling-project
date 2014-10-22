'''
Created on Jul 2, 2014

@author: dbhage

Script to generate author-article table in a csv file
'''

from author.author import get_authors
from util.io import get_lines
from table.author_article import save_author_articles_to_file, last_name_and_one_first_name_present, last_name_present, name_bigram_present, find_authors
from scripts import AUTHOR_NODE_LIST_FOLDER, AUTHOR_ARTICLE_CSV_FNAME
import os, time

BIGRAMS = True # are we using bigrams data or unigrams?

author_files = []
lines = []

print ("Starting:" + str(time.clock()))

# get lines which contain author names
for filee in os.listdir(AUTHOR_NODE_LIST_FOLDER):
    lines += get_lines(AUTHOR_NODE_LIST_FOLDER + filee)

# parse lines and get author names
authors = get_authors(lines)

# folder where articles are found
articles_folder = "ARTICLES FOLDER PATH"

# list of authors for which we can only use last names
last_name_only_list = "goethe balzac proust woolf dickens melville poe diderot flaubert verne stendhal zola fontane hoelderlin kafka novalis rilke schiller wieland"

# get author article table
file_names = sorted(os.listdir(articles_folder))

author_articles = dict()

for article in file_names:
    article_content = open(articles_folder + article).read()
    
    if not BIGRAMS:
        auths = find_authors(authors, article_content, last_name_and_one_first_name_present, last_name_present, last_name_only_list)
    else:
        auths = find_authors(authors, article_content, name_bigram_present, last_name_present, last_name_only_list)

    author_articles[article] = auths


# save author articles to file
save_author_articles_to_file(AUTHOR_ARTICLE_CSV_FNAME, author_articles)

print ("Done:" + str(time.clock()))