'''
Created on Jul 2, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, save_author_topics_to_file, save_author_topics_to_file_beautify, author_topic_counts, save_author_topic_counts_to_file
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
import time
from scripts import COMPOSITIONS_FNAME, AUTHOR_ARTICLE_CSV_FNAME, AUTHOR_TOPIC_CSV_FNAME, AUTHOR_TOPIC_BEAUTIFIED_FNAME, AUTHOR_TOPIC_TABLE_WITH_COUNTS_TABLE_FNAME

print ("Starting:" + str(time.clock()))

compositions = get_compositions(COMPOSITIONS_FNAME)

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

att = author_topic_table(compositions, author_articles)

save_author_topics_to_file(att, AUTHOR_TOPIC_CSV_FNAME)

save_author_topics_to_file_beautify(att, AUTHOR_TOPIC_BEAUTIFIED_FNAME)

count_dict = author_topic_counts(att)

save_author_topic_counts_to_file(count_dict, AUTHOR_TOPIC_TABLE_WITH_COUNTS_TABLE_FNAME)

print ("Done:" + str(time.clock()))