'''
Created on Oct 13, 2014

@author: dbhage

Script to get all author names from the scraped galenet data
'''

from scripts import DROPBOX_FOLDER
from author.galenet.html_parser import get_authors

GALENET_DATA_FOLDER = DROPBOX_FOLDER + "TopicModels/authors/authors_gale_html_only/"

MAX = 237981

i = 1

with open(GALENET_DATA_FOLDER + "author_master_list.txt", 'w')  as fd_out:

    while (i <= MAX):

        print (i)
        fname = GALENET_DATA_FOLDER + "file" + str(i) + ".html"
        i+=10
        
        with open(fname, 'r') as fd_in:
            html_doc = fd_in.read()
            authors = get_authors(html_doc)
            
            for author in authors:
                fd_out.write(author + '\n')          