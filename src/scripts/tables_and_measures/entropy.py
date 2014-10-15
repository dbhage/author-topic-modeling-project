'''
Created on Jul 30, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table, author_topic_list, author_topic_counts
from table.composition import get_compositions
from table.author_article import load_author_article_from_file
from measures.entropy import calculate_entropies, entropy_summation
from measures.common import get_documents_per_author

from scripts import AUTHOR_ARTICLE_CSV_FNAME, COMPOSITIONS_FNAME, ENTROPIES_CSV_FNAME

import time

print ("Starting:" + str(time.clock()))

compositions = get_compositions(COMPOSITIONS_FNAME)

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

att = author_topic_table(compositions, author_articles)

no_of_topics = 300

author_topic_list = author_topic_list(att)

author_topic_count = author_topic_counts(att)

docs_per_auth = get_documents_per_author(author_articles)

entropies = calculate_entropies(docs_per_auth, no_of_topics, author_topic_list, author_topic_count, entropy_summation)

with open(ENTROPIES_CSV_FNAME, 'w') as fd:
    for (k,v) in entropies.items():
        fd.write(str(k))
        fd.write(",")
        fd.write(str(v))
        fd.write('\n')

print ("Done:" + str(time.clock()))