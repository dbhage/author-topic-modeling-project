'''
Created on Sep 15, 2014

@author: dbhage
'''

from corpus.jstor.citations_parser import get_citations
from util.io import get_lines
from scripts import citations_file, compositions_file
from table.composition import get_compositions, save_compositions_to_file
from datetime import date
import time

print ("Starting:" + str(time.clock()))

citations = get_citations(get_lines(citations_file))
citations_dict = dict()

for citation in citations:
    new_id = "bigrams_" + citation.id.replace('/', '_') + ".txt"
    citations_dict[new_id] = citation

compositions = get_compositions(compositions_file)

first_compo_dict = dict()
second_compo_dict = dict()

minimum_date = date(1950,1,1)
threshold = date(1981,1,1)
maximum_date = date(2010,1,1)

for (a_name, composition) in compositions.items():
    citation_date = citations_dict[a_name].pub_date
    if citation_date < threshold and citation_date > minimum_date:
        first_compo_dict[a_name] = composition
    elif citation_date >= threshold and citation_date < maximum_date:
        second_compo_dict[a_name] = composition

# output both files
first_compo_txt_file_name = "/home/dbhage/piperlab/compositions_1950-1980.txt"
second_compo_txt_file_name = "/home/dbhage/piperlab/compositions_1981-2010.txt"

save_compositions_to_file(first_compo_dict, first_compo_txt_file_name)
save_compositions_to_file(second_compo_dict, second_compo_txt_file_name)

print ("Done:" + str(time.clock()))