'''
Created on Jun 26, 2014

@author: dbhage

Module responsible for getting author article table
'''

import re, sys
from author.author import Author

def load_author_article_from_file(csv_file_name):
    '''
    Load author-article table from csv file in a dict
    @param csv_file_name: csv file containing article names and authors in that article
    @return: dict with article id as key and list of Author objects as value
    '''
    author_articles = dict()
    
    with open(csv_file_name, 'r') as fd:
        for line in fd:
            line = line.replace('\n', '')
            line = line.split(',')
            aid = line[0]
            
            authors = []
            
            if len(line) > 1:
                # find authors
                for i in range(1, len(line)):
                    full_name = line[i]

                    if full_name:
                        full_name = full_name.split()
                        author = Author()
                        if len(full_name) > 1:
                            for j in range(0, len(full_name) - 1):
                                author.add_first_name(full_name[j])
                        author.add_last_name(full_name[-1])
                        authors.append(author)
            
            author_articles[aid] = authors
            
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
        print >> sys.stderr, "Error while saving author articles table to csv file."

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

def find_authors_popular(authors, article_content, ignore_list):
    '''
    Find the most popular author in article and the number of occurrences
    
    @param authors: list of AUthor objects
    @type authors: Author[]
    
    @param article_content: string with article content
    @type article_content: str

    @param ignore_list: list of words to ignore when generating bigram combos
    @type ignore_list: str list
     
    @return: 2-tuple containing author object and count
    @rtype: tuple(Author,int)
    '''
    if authors is None or authors == [] or article_content is None or article_content == "":
        return []
    
    article_content = article_content.lower()  

    most_popular_author = (None, -1)

    for author in authors:
        
        count = 0
        bigram_combos = generate_bigram_combos(author, ignore_list)
        
        for bigram_combo in bigram_combos:
            matches = re.findall(r"\b" + re.escape(bigram_combo) + r"\b", article_content)
            if matches:
                count += len(matches)
                
        if count > most_popular_author[1]:
            most_popular_author = (author, count)
    
    return most_popular_author

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

def name_bigram_present(bigram_combos, article_content):
    '''
    Find an author's name in the article by looking for first name and last name bigram combos

    @param bigram_combos: list of bigram combinations
    @type bigram_combos: str list

    @param article_content: the string with the article content
    @type article_content: str

    @return: True if any bigram combos of name present for that particular author is found in the article, False otherwise
    @rtype: boolean
    
    @raise ValueError: if parameter(s) invalid
    '''
    if bigram_combos is None:
        raise ValueError("Bigram Combos invalid")
        
    if not article_content:
        raise ValueError("article content invalid")
    
    if not bigram_combos:
        return False
    
    for bigram_combo in bigram_combos:
        if re.search(r"\b" + re.escape(bigram_combo) + r"\b", article_content):
            return True
    
    return False

def generate_bigram_combos(author, ignore_list):
    '''
    Generate all bigram combinations for author's name
    
    @param author: the Author object representing the author whom we want to find the article
    @type author: Author
    
    @param ignore_list: list of words to ignore
    @type ignore_list: str list
    
    @return: list of all possible bigram combinations for this author
    @rtype: str list
    '''
    if not author or ignore_list is None:
        raise ValueError("Parameters invalid.");
    
    bigram_combos = []
    
    for i in range(0, len(author.first_names)):
        for j in range(0, len(author.last_names)):
            if author.first_names[i] in ignore_list or author.last_names[j] in ignore_list:
                continue
            bigram_combos.append(author.first_names[i] + ' ' + author.last_names[j])
 
    return bigram_combos

def get_last_name_count(article_content, last_name):
    '''
    @param article_content: the content of the article
    @type article_content: str
    
    @param last_name: author's last name
    @type last_name: str
    
    @return: number of matches for last name in article content
    @rtype: int
    
    @raise ValueError: if parameters are invalid
    '''
    if not article_content:
        raise ValueError("article content invalid")
    
    if not last_name:
        raise ValueError("last name invalid")
        
    matches = re.findall(r"\b" + re.escape(last_name) + r"\b", article_content)
    
    if matches:
        return len(matches)
    
    return 0