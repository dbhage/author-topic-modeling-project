'''
Created on Oct 3, 2014

@author: dbhage
'''

from scripts import AUTHOR_NODE_LIST_FOLDER, NODE_FNAME
import os, sys
from util.io import get_lines
from author.author import get_authors

all_lines = dict()

for csv_file in os.listdir(AUTHOR_NODE_LIST_FOLDER):
    
    if not "Novel_Authors" in csv_file:
        continue
    
    print (csv_file)
    lines = get_lines(AUTHOR_NODE_LIST_FOLDER + csv_file)
    
    if not lines:
        print >> sys.stderr, "Failed to read: " + csv_file
        sys.exit(-1)

    authors = get_authors(lines)

    if "English" in csv_file:
        all_lines['english'] = authors
    elif "French" in csv_file:
        all_lines['french'] = authors
    elif "German" in csv_file:
        all_lines['german'] = authors

# output node file
with open(NODE_FNAME, 'w') as csv_file:
    csv_file.write("id,label,language\n")
    for (language, authors) in all_lines.items():
        for author in authors:
            csv_file.write(str(author) + ',' + str(author) + ',' + language + '\n')