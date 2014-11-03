'''
Created on Sep 15, 2014

@author: dbhage
'''

from corpus.jstor.citations_parser import get_citations
from util.io import get_lines
from scripts import CITATIONS_FILE_FNAME, AUTHOR_ARTICLE_CSV_FNAME, UPPER_WORKING_FOLDER
from datetime import date
import time
from table.author_article import load_author_article_from_file, save_author_articles_to_file

print ("Starting:" + str(time.clock()))

citations = get_citations(get_lines(CITATIONS_FILE_FNAME)[1:])
citations_dict = dict()

for citation in citations:
    new_id = "bigrams_" + citation.id.replace('/', '_') + ".txt"
    citations_dict[new_id] = citation

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

first_compo_dict = dict()
second_compo_dict = dict()

minimum_date = date(1950,1,1)
threshold = date(1981,1,1)
maximum_date = date(2010,1,1)

for (a_name, articles) in author_articles.items():
    citation_date = citations_dict[a_name].pub_date
    if citation_date < threshold and citation_date > minimum_date:
        first_compo_dict[a_name] = articles
    elif citation_date >= threshold and citation_date < maximum_date:
        second_compo_dict[a_name] = articles

# output both files
first_compo_txt_file_name = UPPER_WORKING_FOLDER + "1950-1980/author_articles.csv"
second_compo_txt_file_name = UPPER_WORKING_FOLDER + "1981-2010/author_articles.csv"

save_author_articles_to_file(first_compo_txt_file_name, first_compo_dict)
save_author_articles_to_file(second_compo_txt_file_name, second_compo_dict)

print ("Done:" + str(time.clock()))