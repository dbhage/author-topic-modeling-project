'''
Created on Jul 29, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, author_topics_most_dominant
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
from measures.purity import calculate_purities
import sys, time
from scripts import compositions_file, author_article_csv_file, purities_metadata_file, purities_csv_file

print ("Starting:" + str(time.clock()))

compositions = get_compositions(compositions_file)

author_articles = load_author_article_from_file(author_article_csv_file)

att = author_topic_table(compositions, author_articles)

most_dom = author_topics_most_dominant(att)

temp = sys.stdout
sys.stdout = open(purities_metadata_file, 'w')
purities = calculate_purities(author_articles, most_dom)
sys.stdout = temp

with open(purities_csv_file, 'w') as fd:
    for (k,v) in purities.items():
        fd.write(str(k) + ',' + str(v) + '\n')

print ("Done:" + str(time.clock()))