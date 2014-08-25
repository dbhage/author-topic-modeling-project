'''
Created on Aug 11, 2014

@author: dbhage
'''

from table.composition import get_compositions
import sys

print ("Starting")

compositions_file = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/TopicModels/Trial 4/compositions.txt"

compositions = get_compositions(compositions_file)

if compositions:
    with open("/home/dbhage/piperlab/article_topic.csv", 'w') as fd:
        fd.write("article name,main topic\n")
        for (a_name, composition) in compositions.items():
            fd.write(a_name + ',' + str(composition.main_topic) + '\n')
else:
    print >> sys.stderr, "Compositions None"

print ("Done.")