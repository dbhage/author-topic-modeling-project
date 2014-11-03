'''
Created on Nov 3, 2014

@author: dbhage

Run all the scripts in this folder in order.
'''

import subprocess

script_names = ["article_topic", 
                "author_topic_table", 
                "article_pubdate", 
                "author_topic_cooccurrence_list", 
                "author_date_occurrences", 
                "entropy",
                "generate_co_occurrence_list",
                "pubdate_topic",
                "purity",
                "sum_languages"]

for script_name in script_names:
    print ("\nSCRIPT:" + script_name)
    command = ["python", script_name + ".py"]
    subprocess.call(command)