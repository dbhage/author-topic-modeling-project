'''
Created on Oct 31, 2014

@author: dbhage

Generate an article & pub date table
Columns: article id, article pub date, article year
'''

from scripts import CITATIONS_FILE_FNAME, ARTICLE_PUBDATE_FNAME
from corpus.jstor.citations_parser import get_citations_as_dict
from util.io import get_lines

citations = get_citations_as_dict(get_lines(CITATIONS_FILE_FNAME)[1:])

with open(ARTICLE_PUBDATE_FNAME, 'w') as fd:
    fd.write("article id, article pub date, article year\n")
    for (new_id, citation) in citations.items():
        fd.write(new_id + ',' + str(citation.pub_date) + ',' + str(citation.get_year()) + '\n')