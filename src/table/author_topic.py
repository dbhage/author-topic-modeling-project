'''
Created on Jul 1, 2014

@author: dbhage
'''

import sys

def author_topic_table(compositions, author_articles):
    '''
    Produce an author-topic table based on compositions and author article data
    @param compositions: dict with article name as key and composition object as value
    @param author_articles: dict with article name as key and author names list as value
    @return: list of AuthorTopic objects
    '''
    if compositions is None or author_articles is None:
        return []
    
    author_topics = []
    
    for article in compositions.keys():
        for author in author_articles[article]:
            author_topic = AuthorTopic(author, compositions[article].main_topic)
            author_topics.append(author_topic)
    
    return author_topics

def save_author_topics_to_file(author_topics, csv_file_name):
    '''
    Save a list of AuthorTopic objects to a csv file
    @param author_topics: list of AuthorTopic objects
    @param csv_file_name: full csv file name in which to write the data
    '''
    try:
        with open(csv_file_name, 'w') as fd:
            fd.write("topic no, author\n")
            for at in author_topics:
                fd.write(str(at.topic) + ',')
                fd.write(str(at.author).replace(',', ' '))
                fd.write('\n')
    except IOError:
        print >> sys.stderr, "IOError while writing author topics to file " + csv_file_name

def get_count_for_authors(author_topics):
    '''
    @param author_topics: list of AuthorTopic objects
    @return: dict with author name as key and (dict with topic as key and count as value) as value
    '''
    author_data_dict = dict() # (author name, dict(topic, count))
    
    for at in author_topics:
        topic_no = at.topic
        author = at.author
            
        if author not in author_data_dict:
            author_data_dict[author] = dict()
            
        if topic_no not in author_data_dict[author]:
            author_data_dict[author][topic_no] = 1
        else:
            author_data_dict[author][topic_no] += 1
    
    return author_data_dict

def save_author_topics_to_file_beautify(author_topics, text_file_name):
    '''
    Save a list of AuthorTopic objects to a text file
    Saves author names a list of (topic, count) associated with that author.
    @param author_topics: list of AuthorTopic objects
    @param csv_file_name: full text file name in which to write the data
    '''
    with open(text_file_name, 'w') as fd:
        for (k,v) in get_count_for_authors(author_topics).items():
            fd.write(str(k) + ": {")
            for element in sorted(v.items(), key=lambda x: x[1], reverse=True):
                fd.write(str(element[0]) + ":" + str(element[1]) + " ")
            fd.write('}\n')

def author_topics_most_dominant(author_topics):
    '''
    @param author_topics: list of AuthorTopic objects
    @return: dict with author name as key and most dominant topic as value
    '''
    most_dominant_dict = dict()
    for (k,v) in get_count_for_authors(author_topics).items():
        most_dominant_dict[k] = sorted(v.items(), key=lambda x: x[1], reverse=True)[0]
    return most_dominant_dict

def author_topic_list(author_topics):
    '''
    @param author_topics: list of AuthorTopic objects
    @return: dict with author as key and list of topics associated as value
    '''
    atl = dict()
    for (k,v) in get_count_for_authors(author_topics).items():
        atl[k] = v.keys()
    return atl

def author_topic_counts(author_topics):
    '''
    @param author_topics: list of AuthorTopic objects
    @return: dict with AuthorTopic objects as keys and counts as values
    '''
    count_dict = dict()
    for author_topic in author_topics:
        if author_topic in count_dict:
            count_dict[author_topic] += 1
        else:
            count_dict[author_topic] = 1
    return count_dict

def save_author_topic_counts_to_file(count_dict, csv_file_name):
    '''
    Save author-topic-count table to file
    @param count_dict: dict with AuthorTopic objects as keys and counts as values
    @param csv_file_name: csv file's full path where the author-topic-count table will be stored
    '''
    with open(csv_file_name, 'w') as fd:
        fd.write("author,topic,count")
        for (k,v) in count_dict.items():
            fd.write(str(k.author) + "," + str(k.topic) + "," + str(v) + '\n')

class AuthorTopic(object):
    def __init__(self, names, topic):
        self.author = names
        self.topic = topic
    
    def __eq__(self, other):
        return self.author == other.author and self.topic == other.topic
    
    def __str__(self):
        return "Author:" + str(self.author) + " Topic: " + str(self.topic)

    def __hash__(self):
        return hash((self.author, self.topic))