'''
Created on Jul 2, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, save_author_topics_to_file, save_author_topics_to_file_beautify, author_topic_counts, save_author_topic_counts_to_file
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
import time
from scripts import compositions_file, author_article_csv_file, author_topic_csv_file, author_topic_beautified, author_topic_table_with_counts_csv_file

print ("Starting:" + str(time.clock()))

compositions = get_compositions(compositions_file)

author_articles = load_author_article_from_file(author_article_csv_file)

att = author_topic_table(compositions, author_articles)

save_author_topics_to_file(att, author_topic_csv_file)

save_author_topics_to_file_beautify(att, author_topic_beautified)

count_dict = author_topic_counts(att)

save_author_topic_counts_to_file(count_dict, author_topic_table_with_counts_csv_file)

print ("Done:" + str(time.clock()))