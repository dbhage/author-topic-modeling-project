'''
Created on Aug 4, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, author_topic_list, author_topic_counts, author_topics_most_dominant, save_author_topic_counts_to_file, save_author_topics_to_file, save_author_topics_to_file_beautify
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
from measures.entropy import calculate_entropies, entropy_summation
from measures.common import get_documents_per_author
from measures.purity import calculate_purities

print ("Starting")

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 3/compositions.txt"
csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 3/author_articles_small_corpus.csv"

compositions = get_compositions(compositions_file)

author_articles = load_author_article_from_file(csv_file_name)
att = author_topic_table(compositions, author_articles)
no_of_topics = 300

author_topic_list = author_topic_list(att)
author_topic_count = author_topic_counts(att)
docs_per_auth = get_documents_per_author(author_articles)
most_dom = author_topics_most_dominant(att)

purities = calculate_purities(author_articles, most_dom)
entropies = calculate_entropies(docs_per_auth, no_of_topics, author_topic_list, author_topic_count, entropy_summation)

csv_file_name = "/home/dbhage/piperlab/author_topic_table.csv"
save_author_topics_to_file(att, csv_file_name)

text_file_name = "/home/dbhage/piperlab/author_topic_better_representation.txt"
save_author_topics_to_file_beautify(att, text_file_name)

csv_file_name = "/home/dbhage/piperlab/author_topic_table_with_counts.csv"
save_author_topic_counts_to_file(author_topic_count, csv_file_name)

with open("/home/dbhage/piperlab/final_table.csv", 'w') as fd:
    fd.write("author,no of articles,purity,entropy\n")
    for k in entropies.keys():
        fd.write(str(k))
        fd.write(",")
        fd.write(str(docs_per_auth[k]))
        fd.write(",")
        fd.write(str(purities[k]))
        fd.write(",")
        fd.write(str(entropies[k]))
        fd.write('\n')

print ("Done")