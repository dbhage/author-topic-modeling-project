'''
Created on Sep 7, 2014

@author: dbhage
'''

from table.author_article import load_author_article_from_file
from corpus.jstor.citations_parser import get_citations
from util.io import get_lines
from scripts import author_article_csv_file, citations_file, author_date_csv_file

import time

print ("Starting: " + str(time.clock()))

# load dict with article id as key and list of Author objects as value
author_articles = load_author_article_from_file(author_article_csv_file)

# citations
citations = get_citations(get_lines(citations_file))
citations_dict = dict()

for citation in citations:
    new_id = "bigrams_" + citation.id.replace('/', '_') + ".txt"
    citations_dict[new_id] = citation

author_date_list = []

for (article, authors) in author_articles.items():
    for author in authors:
        author_date_list.append((str(author), str(citations_dict[article].pub_date)))
        
with open(author_date_csv_file, 'w') as fd:
    for (auth, date) in author_date_list:
        fd.write(auth + ',' + date + '\n')

print ("Done: " + str(time.clock()))