'''
Created on Oct 3, 2014

@author: dbhage

can you transform the following table:

author_articles.csv

and substitute language for the author name?

so where it says edgar allen poe, substitute english

use the full list of author names from here:

authors/list/Novel_Authors_English.csv
authors/list/Novel_Authors_French.csv
authors/list/Novel_Authors_German.csv

then please calculate the following:

A. total number of articles
B. total number of articles with at least one author
C. total number of articles with at least two authors
D. % of articles with two different nationalities
E. % of articles with >=2 languages in the articles having >=2 authors
'''

from table.author_article import load_author_article_from_file
from scripts import AUTHOR_ARTICLE_CSV_FNAME, NODE_FNAME
from util.io import get_lines
from measures.cooccurrence.sum_languages import get_node_dict
from measures.author_article.calculations import AuthorArticleCalculation

# get author articles
author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

# get node list
lines = get_lines(NODE_FNAME)
node_dict = get_node_dict(lines)

# perform calculations
author_article_calculation = AuthorArticleCalculation(author_articles, node_dict)

# output
print ("""A. total number of articles: %d
B. total number of articles with at least one author: %d
C. total number of articles with at least two authors: %d
D. # of articles with >=2 languages / total number of articles: %f
E. # of articles with >=2 languages / # articles having >=2 authors: %f
""") % (author_article_calculation.get_no_of_articles(), 
        author_article_calculation.get_no_of_articles_with_atleast_n_authors(1),
        author_article_calculation.get_no_of_articles_with_atleast_n_authors(2),
        author_article_calculation.get_percentage_articles_with_2_langs(),
        author_article_calculation.get_percentage_articles_with_2_langs_2_auths())