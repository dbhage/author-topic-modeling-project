'''
Created on Oct 20, 2014

@author: dbhage
'''


from author.galenet.author_name_parser import get_authors
from util.io import get_lines
from table.author_article import get_author_articles_most_popular
from scripts import GALENET_AUTHOR_MASTER_LIST_FNAME, AUTHOR_ARTICLE_MOST_POPULAR_CSV_FNAME
import time

print ("Starting:" + str(time.clock()))

lines = []

# get lines which contain author names
# use galenet
lines = get_lines(GALENET_AUTHOR_MASTER_LIST_FNAME)

# parse lines and get author names
authors = get_authors(lines)

# folder where articles are found
articles_folder = "/Volumes/New HD/data/Lang_Lit_Lang_Lit_Bigrams/bigrams_expanded/"

ignore_list = ["the", "of", "de", "th", "la", "le"]

# get author article table
with open(AUTHOR_ARTICLE_MOST_POPULAR_CSV_FNAME, 'a') as fd:
    get_author_articles_most_popular(articles_folder, authors, fd, ignore_list)

print ("Done:" + str(time.clock()))