'''
Created on Jul 2, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table
from table.composition import get_compositions
from table.author_article import load_author_article_from_file

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Small Corpus 300 Topics/compositions.txt"
csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/author_articles_small_corpus.csv"

compositions = get_compositions(compositions_file)
author_articles = load_author_article_from_file(csv_file_name)

att = author_topic_table(compositions, author_articles)

csv_file_name = "/home/dbhage/piperlab/att.csv"

with open(csv_file_name, 'w') as fd:
    fd.write("topic no, author\n")
    for at in att:
        fd.write(str(at.topic) + ',')
        fd.write(str(at.author).replace(',', ' '))
        fd.write('\n')