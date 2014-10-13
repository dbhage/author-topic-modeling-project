'''
Created on Jul 29, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, author_topics_most_dominant
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
from measures.purity import calculate_purities
import sys, time
from scripts import COMPOSITIONS_FNAME, AUTHOR_ARTICLE_CSV_FNAME, PURITIES_METADATA_FNAME, PURITIES_CSV_FNAME

print ("Starting:" + str(time.clock()))

compositions = get_compositions(COMPOSITIONS_FNAME)

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

att = author_topic_table(compositions, author_articles)

most_dom = author_topics_most_dominant(att)

temp = sys.stdout
sys.stdout = open(PURITIES_METADATA_FNAME, 'w')
purities = calculate_purities(author_articles, most_dom)
sys.stdout = temp

with open(PURITIES_CSV_FNAME, 'w') as fd:
    for (k,v) in purities.items():
        fd.write(str(k) + ',' + str(v) + '\n')

print ("Done:" + str(time.clock()))