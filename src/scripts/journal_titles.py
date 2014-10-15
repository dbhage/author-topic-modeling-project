'''
Created on Oct 15, 2014

@author: dbhage

Get list of journal titles from jstor bigram corpus
'''

from scripts import CITATIONS_FILE_FNAME, JOURNAL_LIST_FILE_NAME
from corpus.jstor.citations_parser import get_citations
from util.io import get_lines

lines = get_lines(CITATIONS_FILE_FNAME)
citations = get_citations(lines)

journal_titles = set()

for citation in citations:
    journal_titles.add(citation.journal_title)

print (len(journal_titles))

with open(JOURNAL_LIST_FILE_NAME, 'w') as fd:
    fd.write('\n'.join(journal_titles))