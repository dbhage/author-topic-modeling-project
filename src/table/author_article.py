'''
Created on Jun 26, 2014

@author: dbhage
'''

import re, os, sys
from author.author import Author

def get_author_articles(articles_folder, authors, last_name_only_list, num=-1):
    '''
    Get author-article table in the form of a dict
    @param articles_folder: folder containing articles in text files
    @param authors: list of Author objects
    @param last_name_only_list: list of authors for whom we can only search the last name
    @param num: int for number of files. if < 0 or > no of articles in article_folder, all article files are used
    @return: dict with article name as key and list of authors present in that article as value
    '''
    file_names = sorted(os.listdir(articles_folder))

    if num < 0 or num >= len(file_names):
        num = len(file_names)
    
    author_articles = dict()
    
    for article in file_names[:num]:
        article_content = open(articles_folder + article).read()
        auths = find_authors(authors, article_content, last_name_and_one_first_name_present, last_name_present, last_name_only_list)
        author_articles[article] = auths
    
    return author_articles

def load_author_article_from_file(csv_file_name):
    '''
    Load author-article table from csv file in a dict
    @param csv_file_name: csv file containing article names and authors in that article
    @return: dict with article id as key and list of Author objects as value
    '''
    author_articles = dict()
    
    with open(csv_file_name, 'r') as fd:
        lines = fd.readlines()
        
        for line in lines:
            line = line.split(',')
            article = line[0]
            
            authors = []
            
            if len(line) > 1:
                for i in range(1, len(line)-1):
                    full_name = line[i].split()
                    author = Author()
                    author.add_last_name(full_name[0])
                    author.add_first_names(full_name[1:])
                    authors.append(author)
                
            author_articles[article] = authors
    
    return author_articles

def save_author_articles_to_file(csv_file_name, aa_table):
    '''
    Save author-article table to csv file
    @param aa_table: author-article table
    @param csv_file_name: csv file to write to
    '''
    try:
        with open(csv_file_name, 'w') as fd:
            for (k,v) in aa_table.items():
                fd.write(k)
                fd.write(',')
                for i in range(0, len(v)):
                    fd.write(str(v[i]).replace(',', ' '))
                    if i != len(v) - 1:
                        fd.write(',')
                fd.write('\n')    
    except IOError:
        print >> sys.stderr, "Erro while saving author articles table to csv file."

def find_authors(authors, article_content, lnaofnp_func, lnp_func, last_name_only_list):
    '''
    Find if author in article 
    @param authors: list of authors
    @param article_content: content of article in which we want to find author
    @param lnaofnp_func: last name and only one first name present function
    @param lnp_func: last name present function
    @return: list of authors found in article_content
    '''
    if authors is None or authors == [] or article_content is None or article_content == "":
        return []
    
    article_content = article_content.lower()
    
    matches = []
    
    for author in authors:
        last_name_in_list = False
        
        for last_name in author.last_names:
            if last_name in last_name_only_list:
                last_name_in_list = True
        
        if not last_name_in_list:
            if lnaofnp_func(author, article_content):
                matches.append(author)
        else:
            if lnp_func(author, article_content):
                matches.append(author)
    
    return matches

def last_name_present(author, article_content):
    '''
    Find an author's last names in the article
    @param author: the Author object representing the author whom we want to find the article
    @param article_content: the string with the article content
    @return: True if all last names for that particular author is found in the article, False otherwise
    '''
    if author is None or article_content is None or article_content == "":
        return False

    count = 0
    for last_name in author.last_names:
        if re.search(r'\b' + re.escape(last_name) + r'\b', article_content):
            count += 1
    return count == len(author.last_names)

def last_name_and_one_first_name_present(author, article_content):
    '''
    Find an author's last names and at least 1 first name in the article
    @param author: the Author object representing the author whom we want to find the article
    @param article_content: the string with the article content
    @return: True if all last names & atleast 1 first name for that particular author is found in the article, False otherwise.
    '''
    if author is None or article_content is None or article_content == "":
        return False

    count_last = 0
    
    for last_name in author.last_names:
        if re.search(r'\b' + re.escape(last_name) + r'\b', article_content):
            count_last += 1
            
    one_first_name_present = False

    for first_name in author.first_names:
        if re.search(r'\b' + re.escape(first_name) + r'\b', article_content):
            one_first_name_present = True
    
    return count_last == len(author.last_names) and one_first_name_present

def full_name_present(author, article_content):
    '''
    Find an author's full name in the article
    @param author: the Author object representing the author whom we want to find the article
    @param article_content: the string with the article content
    @return: True if full name for that particular author is found in the article, False otherwise
    '''
    if author is None or article_content is None or article_content == "":
        return False
    
    count_last = 0
    
    for last_name in author.last_names:
        if re.search(r'\b' + re.escape(last_name) + r'\b', article_content):
            count_last += 1
            
    count_first = 0

    for first_name in author.first_names:
        if re.search(r'\b' + re.escape(first_name) + r'\b', article_content):
            count_first += 1
    
    return count_last == len(author.last_names) and count_first == len(author.first_names)   