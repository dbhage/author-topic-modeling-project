'''
Created on Oct 16, 2014

@author: dbhage

Make come calculations on Goethe only, to validate our results.
'''

from measures.cooccurrence.sum_languages import get_node_dict
from util.io import get_lines
from scripts import NODE_FNAME
from table.author_article import load_author_article_from_file
from scripts import AUTHOR_ARTICLE_CSV_FNAME
from author.author import Author

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

goethe = Author()
goethe.add_first_name("johann")
goethe.add_last_name("goethe")

count = 0
count_german = 0
goether_general_occ = 0
german_authors = set()

lines = get_lines(NODE_FNAME)
node_dict = get_node_dict(lines)

for (article, authors) in author_articles.items():
    if goethe in authors:
        goether_general_occ += 1
    if len(authors) >= 2 and goethe in authors:
        count += 1
        for author in authors:
            if author != goethe:
                if node_dict[str(author)] == "german":
                    count_german += 1
                    german_authors.add(str(author))

print (count)
print (count_german)
print (len(german_authors))
print (german_authors)
print (goether_general_occ)