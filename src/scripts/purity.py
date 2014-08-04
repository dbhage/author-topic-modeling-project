'''
Created on Jul 29, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, author_topics_most_dominant
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
from measures.purity import calculate_purities
import sys

print ("Starting")

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 3/compositions.txt"

csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 3/author_articles_small_corpus.csv"

compositions = get_compositions(compositions_file)

author_articles = load_author_article_from_file(csv_file_name)

att = author_topic_table(compositions, author_articles)

most_dom = author_topics_most_dominant(att)

temp = sys.stdout
sys.stdout = open("/home/dbhage/piperlab/purities_metadata.txt", 'w')
purities = calculate_purities(author_articles, most_dom)
sys.stdout = temp

with open("/home/dbhage/piperlab/purities.csv", 'w') as fd:
    for (k,v) in purities.items():
        fd.write(str(k) + ',' + str(v) + '\n')

print ("Done")