'''
Created on Sep 7, 2014

@author: dbhage
'''

from table.author_article import load_author_article_from_file
from corpus.jstor.citations_parser import get_citations
from util.io import get_lines

import time

print ("Starting: " + str(time.clock()))

csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 4/author_articles_small_corpus.csv"

# load dict with article id as key and list of Author objects as value
author_articles = load_author_article_from_file(csv_file_name)

# citations
citations_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/citations.CSV"
citations = get_citations(get_lines(citations_file))
citations_dict = dict()

for citation in citations:
    new_id = "wordcounts_" + citation.id.replace('/', '_') + ".txt"
    if new_id in citations_dict:
        raise Exception(new_id + " should not be in dict")
    else:
        citations_dict[new_id] = citation

author_date_list = []

for (article, authors) in author_articles.items():
    for author in authors:
        author_date_list.append((str(author), str(citations_dict[article].pub_date)))
        
output_file = "/home/dbhage/piperlab/author_date.csv"

with open(output_file, 'w') as fd:
    for (auth, date) in author_date_list:
        fd.write(auth + ',' + date + '\n')

print ("Done: " + str(time.clock()))