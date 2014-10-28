'''
Created on Oct 28, 2014

@author: dbhage

Measure precision and recall for author articles using the validation sample produced by the RA
'''

from table.author_article import load_author_article_from_file
from scripts import AUTHOR_ARTICLE_CSV_FNAME, AUTHOR_MASTER_LIST_CSV_FNAME, AA_BIGRAM_VALIDATION_FILE
from measures.relevance_scores import precision, recall, accuracy
from measures.author_article.accuracy import measure_sns
from author.names import extract_author_names
from author.author import Author, get_authors
from util.io import get_lines

# get author list
lines = get_lines(AUTHOR_MASTER_LIST_CSV_FNAME)

# parse lines and get author names
author_list = get_authors(lines)

# get actual author articles
actual_author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

# get expected author articles
expected_author_articles = {}

non_existing_authors = set()

fd = open(AA_BIGRAM_VALIDATION_FILE, 'r')

for line in fd:
    line = line.split(',')
    
    article_name = "bigrams_10.2307_" + line[0] + ".txt"
    author_names = extract_author_names(line[3])

    if not author_names:
        continue
    
    if "E.M.Forster" in line[3]:
        author_names = ['e.m.', "forster"]
    
    if "D.H.Lawrence" == line[3]:
        author_names = ['d.h.', "lawrence"]

    author = Author()
    author.add_last_name(author_names[-1])
    author.add_first_names(author_names[0:len(author_names)-1])

    if not author in author_list:
        non_existing_authors.add(author)
        continue

    if not article_name in expected_author_articles:
        expected_author_articles[article_name] = []

    expected_author_articles[article_name].append(author)

print ("Unrecognized Authors: " + ','.join([str(auth) for auth in non_existing_authors]))
print ("------")

# measure precision and recall
(tp, fp, fn, tn) = measure_sns(actual_author_articles, expected_author_articles, author_list)

print ("tp,fp,fn,tn:" + str((tp, fp, fn, tn)))

precision_value = precision(tp, fp)
recall_value = recall(tp, fn)
accuracy_value = accuracy(tp, tn, fp, fn)

print ("Precision: "),
print (precision_value)

print ("Recall: "),
print (recall_value)

print ("Accuracy Value: "),
print (accuracy_value)