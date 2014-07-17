'''
Created on Jul 16, 2014

@author: dbhage
'''

from measures.author_name_recognition import anr_comparison_string, get_validated_data
from table.author_article import load_author_article_from_file

piperlab_dir = "/home/dbhage/piperlab/"
dropbox_dir = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/"

aa_csv_file_name = dropbox_dir + "Trial 2/author_articles_small_corpus.csv"

generated_data = load_author_article_from_file(aa_csv_file_name)

validated_data_files = [dropbox_dir + "authors/AuthourValidationSearchedComplete.csv", 
                        dropbox_dir + "authors/RandomAuthorValidationComplete.csv"]

lines = []

for filee in validated_data_files:
    with open(filee, 'r') as fd:
        lines += fd.readlines()

validated_data = get_validated_data(lines)

with open(piperlab_dir + "anr_comp.csv", 'w') as fd:
    fd.write(anr_comparison_string(validated_data, generated_data))