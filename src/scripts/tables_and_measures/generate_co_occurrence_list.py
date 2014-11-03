'''
Created on Aug 25, 2014

@author: dbhage
'''

from table.author_article import load_author_article_from_file
from scripts import AUTHOR_ARTICLE_CSV_FNAME, COOCCURRENCE_LIST_FNAME, AUTHOR_COOCCURRENCE_EDGE_LIST_PLUS10
from author.co_occurrence.co_occurrence import get_co_occurrence_list, get_co_occurrence_dict, list_all_co_occurences
import time

print ("Starting:" + str(time.clock()))

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

co_occ_dict = get_co_occurrence_dict(author_articles, list_all_co_occurences)
co_occ_list = get_co_occurrence_list(co_occ_dict)

with open(COOCCURRENCE_LIST_FNAME, 'w') as fd_coocc_full, open(AUTHOR_COOCCURRENCE_EDGE_LIST_PLUS10, 'w') as fd_coocc_plus_10:
    fd_coocc_full.write("auth1, auth2, weight\n")
    fd_coocc_plus_10.write("auth1, auth2, weight\n")
    for co_occ in co_occ_list:
        if co_occ[0] == co_occ[1]:
            raise Exception("author cooccurs with him/her-self:" + str(co_occ[0]))
        if co_occ[2] >= 10:
            fd_coocc_plus_10.write(co_occ[0] + ',' + co_occ[1] + ',' + str(co_occ[2]) + '\n')
        fd_coocc_full.write(co_occ[0] + ',' + co_occ[1] + ',' + str(co_occ[2]) + '\n')

print ("Done:" + str(time.clock()))