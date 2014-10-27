'''
Created on Oct 22, 2014

@author: dbhage

Script to obtain for each article, the author who has a bigram presence and whose last name occurs most
Generates a table with <article name, author name, last name count>
'''

from author.galenet.author_name_parser import get_authors
from util.io import get_lines
from scripts import GALENET_AUTHOR_MASTER_LIST_FNAME, AUTHOR_ARTICLE_LNC_CSV_FNAME, CITATIONS_FILE_FNAME, ARTICLES_FOLDER
import time, os
from table.author_article import name_bigram_present, get_last_name_count, generate_bigram_combos
from corpus.jstor.citations_parser import get_citations

print ("Starting:" + str(time.clock()))

lines = []

# get lines which contain author names
# use galenet
lines = get_lines(GALENET_AUTHOR_MASTER_LIST_FNAME)

# parse lines and get author names
authors = get_authors(lines)

print ("#authors: " + str(len(authors)))

# list of words to be ignored
ignore_list = ["the", "of", "de", "th", "la", "le", "", "in", "an"]

# get citations
citations = get_citations(get_lines(CITATIONS_FILE_FNAME))
citations_dict = dict()

for citation in citations:
    new_id = "bigrams_" + citation.id.replace('/', '_') + ".txt"
    citations_dict[new_id] = citation

print ("Citations loaded.\n")

# get author article table
with open(AUTHOR_ARTICLE_LNC_CSV_FNAME, 'w') as fd:
    fd.write("article id, author, LNC, article title\n")
    
    file_names = sorted(os.listdir(ARTICLES_FOLDER))

    for article in file_names:
        if article == ".DS_Store":
            continue
        
        print (article)
        
        article_content = open(ARTICLES_FOLDER + article).read()
        
        max_auth_tup = (None,-1)
        
        for author in authors:
            bigram_combos = generate_bigram_combos(author, ignore_list)
            
            if name_bigram_present(bigram_combos, article_content):
                # bigram present
                lnc = get_last_name_count(article_content, author.last_names[0])
                
                if (lnc > max_auth_tup[1]):
                    # is count > what we already have?
                    max_auth_tup = (author, lnc)
        
        if max_auth_tup[1] == -1:
            # nothing matched
            max_auth_tup = ("NA", "NA")
        
        print ('\t'),
        print (str(max_auth_tup[0]) + ' -> ' + str(max_auth_tup[1]))
        
        # output row <article file name, author name, number of occurrences of author's last name, article title>
        fd.write(article + ',' + str(max_auth_tup[0]) + ',' + str(max_auth_tup[1]) + ',' + citations_dict[article].title.replace(',', ';') + '\n')

print ("Done:" + str(time.clock()))