'''
Created on Aug 11, 2014

@author: dbhage
'''

from table.composition import get_compositions
from scripts import ARTICLE_COPY_CSV_FNAME, COMPOSITIONS_FNAME
import sys, time

print ("Starting:" + str(time.clock()))

compositions = get_compositions(COMPOSITIONS_FNAME)

if compositions:
    with open(ARTICLE_COPY_CSV_FNAME, 'w') as fd:
        fd.write("article name,main topic\n")
        for (a_name, composition) in compositions.items():
            fd.write(a_name + ',' + str(composition.main_topic) + '\n')
else:
    print >> sys.stderr, "Compositions None"

print ("Done:" + str(time.clock()))