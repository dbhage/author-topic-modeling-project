'''
Created on Oct 27, 2014

@author: dbhage

Run a simple keyword frequency test for all articles according to the following keywords:
transnational
international
national
global
author

Calculate the percentage of times each of these terms appears as a function of total number of words per year.
Find all occurrences of each word for each article, sum those amounts by year, and divide by total number of tokens for any given year.

Output = {
Rows: years,
Columns: keywords,
Values: frequencies of occurrence (keyword occurrences/total word occurrences)}
'''

from corpus.jstor.citations_parser import get_citations_as_dict
from scripts import CITATIONS_FILE_FNAME, ARTICLES_FOLDER, KEYWORDS_OUTPUT_FILE
from util.io import get_lines
import os, re
from measures.keyword_article.keyword_article import KeywordArticle

# get citations
citations = get_citations_as_dict(get_lines(CITATIONS_FILE_FNAME))

# keywords list
keywords_list = ["transnational", "international", "national", "global", "author"]

# regular expressions dict
regex_dict = {k : re.compile(r"\b" + re.escape(k) + r"\b", re.IGNORECASE) for k in keywords_list}

# article file names
fnames = sorted(os.listdir(ARTICLES_FOLDER))

master_dict = {}

# for all articles, get the year, sum up the #occurrences of keywords by year
# we also keep track of the set of unique tokens for all years
print ("Get sums of keywords subset by year")

for fname in fnames:
    if "DS_Store" in fname:
        continue
    
    print ('\t' + fname),
    
    # get that article's year
    # if that year is not present in master dictionary
    #     add it
    year = citations[fname].get_year()
    
    print (" -> " + str(year))
    
    if not year in master_dict:
        master_dict[year] = KeywordArticle(keywords_list, year)
    
    # get content
    with open(ARTICLES_FOLDER + fname, 'r') as fd:
        content = fd.read()
    
    # find keywords and add # occurrences if any
    for (keyword, regex) in regex_dict.items():
        matches = re.findall(regex, content)
        if matches:
            master_dict[year].add_to_keyword(keyword, len(matches))
    
    # merge the set of tokens we have for that year with the tokens from the current article
    master_dict[year].add_to_tokens(content.split(' '))    
    
    # increment # articles
    master_dict[year].no_of_articles += 1

# divide keywords occurrences by #tokens
print ("divide keywords occurrences by #tokens")

for keyword_article in master_dict.values():
    keyword_article.normalize()
    
# output to file
print ("output to file")

with open(KEYWORDS_OUTPUT_FILE, 'w') as fd:
    # write headers
    fd.write('year/keyword,' + ','.join(keywords_list) + '\n')
    
    # write rows
    for keyword_article in master_dict.values():
        fd.write(str(keyword_article))

print ("Done outputting to:" + KEYWORDS_OUTPUT_FILE)