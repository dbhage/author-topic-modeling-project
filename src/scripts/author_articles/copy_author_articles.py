'''
Created on Sep 24, 2014

@author: dbhage
'''

from table.author_article import load_author_article_from_file, save_author_articles_to_file
from scripts import AUTHOR_ARTICLE_CSV_FNAME, AUTHOR_ARTICLE_CSV_COPY_FNAME

save_author_articles_to_file(AUTHOR_ARTICLE_CSV_COPY_FNAME, load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME))