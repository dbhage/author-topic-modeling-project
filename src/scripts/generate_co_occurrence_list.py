'''
Created on Aug 25, 2014

@author: dbhage
'''

from table.author_article import load_author_article_from_file

from author.co_occurrence.co_occurrence import get_co_occurrence_list, get_co_occurrence_dict, list_all_co_occurences

print ("Starting")

csv_file_name = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 4/author_articles_small_corpus.csv"
output_file = "/home/dbhage/piperlab/cooccurrence_list.csv"

author_articles = load_author_article_from_file(csv_file_name)
co_occ_dict = get_co_occurrence_dict(author_articles, list_all_co_occurences)
co_occ_list = get_co_occurrence_list(co_occ_dict)

with open(output_file, 'w') as fd:
    fd.write("auth1, auth2, weight\n")
    for co_occ in co_occ_list:
        fd.write(co_occ[0] + ',' + co_occ[1] + ',' + str(co_occ[2]) + '\n')

print ("Done")