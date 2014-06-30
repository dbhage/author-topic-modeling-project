'''
Created on Jun 26, 2014

@author: dbhage
'''

def find_authors(authors, article_content, dictionary):
    '''
    Find if author in article 
    @param authors: list of authors
    @param article_content: content of article in which we want to find author
    @param dictionary: dictionary of words in the form of a list of dict or Celex object.
    @return: list of authors first_name_found in article_content
    '''
    if authors is None or authors == [] or article_content is None or article_content == "" or dictionary is None:
        return []
    
    article_content = article_content.lower()
    
    matches = []
    
    for author in authors:
        last_name_in_dictionary = False
        
        for last_name in author.last_names:
            if last_name in dictionary:
                last_name_in_dictionary = True
        
        if last_name_in_dictionary:
            if last_name_and_one_first_name_present(author, article_content):
                matches.append(author)
        else:
            if last_name_present(author, article_content):
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
        if last_name in article_content:
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
        if last_name in article_content:
            count_last += 1
            
    one_first_name_present = False

    for first_name in author.first_names:
        if first_name in article_content:
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
        if last_name in article_content:
            count_last += 1
            
    count_first = 0

    for first_name in author.first_names:
        if first_name in article_content:
            count_first += 1
    
    return count_last == len(author.last_names) and count_first == len(author.first_names)   