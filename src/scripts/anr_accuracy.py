'''
Created on Jul 16, 2014

@author: dbhage
'''

from measures.author_name_recognition import anr_comparison_string, get_validated_data
from measures.author_name_recognition import anr_accuracy
from table.author_article import load_author_article_from_file

piperlab_dir = "/home/dbhage/piperlab/"
dropbox_dir = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/"

aa_csv_file_name = dropbox_dir + "Trial 2/author_articles_small_corpus.csv"

comparison_string_enabled = True
anr_acc_string_enabled = True

generated_data = load_author_article_from_file(aa_csv_file_name)

validated_data_files = [dropbox_dir + "authors/AuthourValidationSearchedComplete.csv", 
                        dropbox_dir + "authors/RandomAuthorValidationComplete.csv"]

lines = []

for filee in validated_data_files:
    with open(filee, 'r') as fd:
        lines += fd.readlines()

validated_data = get_validated_data(lines, append_to_id=".txt", prepend_to_id="wordcounts_10.2307_")

if comparison_string_enabled:
    with open(piperlab_dir + "anr_comp_sig.csv", 'w') as fd:
        fd.write(anr_comparison_string(validated_data, generated_data))

if anr_acc_string_enabled:
    anr_acc_string = anr_accuracy(validated_data, generated_data)
    with open(piperlab_dir + "anr_accuracy_matches_sig.txt", 'w') as fd:
        fd.write(anr_acc_string)

print("done")