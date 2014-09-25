'''
Created on Sep 24, 2014

@author: dbhage
'''

from table.author_article import load_author_article_from_file, save_author_articles_to_file
from scripts import author_article_csv_file, author_article_csv_file_copy

save_author_articles_to_file(author_article_csv_file_copy, load_author_article_from_file(author_article_csv_file))