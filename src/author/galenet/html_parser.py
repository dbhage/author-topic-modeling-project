'''
Created on Oct 8, 2014

@author: dbhage

Module responsible for parsing html scraped from galenet website to extract author names. Uses the python bs4 library.
'''

from bs4 import BeautifulSoup
from author.galenet import ampersand_alphabets_semicolon_pattern, alphabet_re, space_re
import re

def get_authors(html_doc):
    '''
    @param html_doc: String representing HTML
    @return: (first names list, last names list) 2-tuples for each author in a list
    '''
    soup = BeautifulSoup(html_doc)
    table = soup.find_all("table")[1]
    trs = table.find_all("tr")
    
    authors = []
    
    for i,tr in enumerate(trs):
        if i == 0 or i == len(trs) - 1: continue
        author = get_author(tr)
        if author:
            authors.append(author)
    
    return authors

def get_author(tr):
    '''
    Get author from tr tag
    @param tr: text in tr tag
    @return: (first names list, last names list) 2-tuple
    '''
    text = tr.get_text()

    if not re.findall(alphabet_re, text):
        return None

    text = re.sub(space_re, ' ', text)
    text = ampersand_alphabets_semicolon_pattern.sub(r"\1", text)

    return text.lower()