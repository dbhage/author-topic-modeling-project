'''
Created on Oct 20, 2014

@author: dbhage

Script to obtain the "most popular" authors in the articles.
We use the Galenet author list and for each article, we find the author whose name gets the most bigram matches.
A table of <article name, author, #bigram occurrences> is output.
'''

from author.galenet.author_name_parser import get_authors
from util.io import get_lines
from scripts import GALENET_AUTHOR_MASTER_LIST_FNAME, AUTHOR_ARTICLE_MOST_POPULAR_CSV_FNAME
import time, os
from table.author_article import find_authors_popular

print ("Starting:" + str(time.clock()))

lines = []

# get lines which contain author names
# use galenet
lines = get_lines(GALENET_AUTHOR_MASTER_LIST_FNAME)

# parse lines and get author names
authors = get_authors(lines)

# folder where articles are found
articles_folder = "/Volumes/New HD/data/Lang_Lit_Lang_Lit_Bigrams/bigrams_expanded/"

# list of words to be ignored
ignore_list = ["the", "of", "de", "th", "la", "le", "", "in", "an"]

# get author article table
with open(AUTHOR_ARTICLE_MOST_POPULAR_CSV_FNAME, 'w') as fd:
    file_names = sorted(os.listdir(articles_folder))

    for article in file_names:
        if article == ".DS_Store":
            continue
        
        print (article)
        
        article_content = open(articles_folder + article).read()
        auth_tup = find_authors_popular(authors, article_content, ignore_list)
        
        if auth_tup[1] == -1:
            auth_tup = ("NA", "NA")
        
        fd.write(article + ',' + str(auth_tup[0]) + ',' + str(auth_tup[1]) + '\n')

print ("Done:" + str(time.clock()))