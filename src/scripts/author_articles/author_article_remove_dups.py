'''
Created on Sep 24, 2014

@author: dbhage
'''

from table.author_article import save_author_articles_to_file, load_author_article_from_file
from scripts import AUTHOR_ARTICLE_CSV_FNAME, AUTHOR_ARTICLE_CSV_COPY_FNAME

author_articles = load_author_article_from_file(AUTHOR_ARTICLE_CSV_FNAME)

new_author_articles = {}

for (k,v) in author_articles.items():
    if v:
        new_auths = [v[0]]
        for i in range(1, len(v)):
            no_dups = True
            for j in range(0, len(new_auths)):
                if v[i] == new_auths[j]:
                    no_dups=False
                    break
            if no_dups:
                new_auths.append(v[i])
        new_author_articles[k] = new_auths
    else:
        new_author_articles[k] = []
    
save_author_articles_to_file(AUTHOR_ARTICLE_CSV_COPY_FNAME, new_author_articles)