'''
Created on Jul 2, 2014

@author: dbhage
'''

from table.author_topic import author_topic_table
from table.composition import get_compositions
from table.author_article import load_author_article_from_file

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Small Corpus 300 Topics/compositions.txt"
csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 1/author_articles_small_corpus.csv"

#compositions = get_compositions(compositions_file)
#author_articles = load_author_article_from_file(csv_file_name)

#att = author_topic_table(compositions, author_articles)

csv_file_name = "/home/dbhage/piperlab/author_topic_table.csv"

'''
with open(csv_file_name, 'w') as fd:
    fd.write("topic no, author\n")
    for at in att:
        fd.write(str(at.topic) + ',')
        fd.write(str(at.author).replace(',', ' '))
        fd.write('\n')
'''     

def get_count_for_authors():
    author_data_dict = dict() # (author name, dict(topic, count))
    
    with open(csv_file_name, 'r') as fd:
        lines = fd.readlines()
        
        for line in lines[1:]:
            line = line.split(',')
            topic_no = int(line[0])
            author = line[1].replace("\n", '')
            
            if author not in author_data_dict:
                author_data_dict[author] = dict()
            
            if topic_no not in author_data_dict[author]:
                author_data_dict[author][topic_no] = 1
            else:
                author_data_dict[author][topic_no] += 1
    
    return author_data_dict

with open("/home/dbhage/piperlab/author_topic_better_representation.txt", 'w') as fd:
    for (k,v) in get_count_for_authors().items():
        fd.write(k + ": {")
        for element in sorted(v.items(), key=lambda x: x[1], reverse=True):
            fd.write(str(element[0]) + ":" + str(element[1]) + " ")
        fd.write('}\n')