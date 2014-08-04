'''
Created on Jul 2, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, save_author_topics_to_file, save_author_topics_to_file_beautify, author_topic_counts, save_author_topic_counts_to_file
from table.composition import get_compositions
from table.author_article import load_author_article_from_file

print ("Starting")

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 3/compositions.txt"

csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 3/author_articles_small_corpus.csv"

compositions = get_compositions(compositions_file)

author_articles = load_author_article_from_file(csv_file_name)

att = author_topic_table(compositions, author_articles)

csv_file_name = "/home/dbhage/piperlab/author_topic_table.csv"

save_author_topics_to_file(att, csv_file_name)

text_file_name = "/home/dbhage/piperlab/author_topic_better_representation.txt"

save_author_topics_to_file_beautify(att, text_file_name)

csv_file_name = "/home/dbhage/piperlab/author_topic_table_with_counts.csv"

count_dict = author_topic_counts(att)

save_author_topic_counts_to_file(count_dict, csv_file_name)

print ("Done")