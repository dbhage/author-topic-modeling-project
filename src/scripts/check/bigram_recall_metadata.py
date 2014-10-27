'''
Created on Oct 27, 2014

@author: dbhage

Test the number of cases in which an author's last name is present in an article that the bigram is also present. 

In other words, we can assume our precision is 100% (when "Herman Melville" is mentioned Herman Melville is in the article).

but can we get an estimate on our recall (how many articles in which "Melville" appears in which "Herman Melville" does not -- and of those how many are talking about Herman Melville)?

1. take the example of Melville.

2. find the number of articles in which the one gram "Melville" occurs.

3. find the number of those articles in 2 in which the bigram "Herman Melville" appears.

This will be our first estimated recall rate.

Then I can have the students go in and read a sample of those articles with "Melville" but not "Herman Melville" and see if there are any false positives -- that it is about a different "Melville."

This will be our second estimated recall rate.

It doesn't capture all cases, but that's impossible anyway. We want just some idea how good the bigram is as a proxy. 

Undercounting is better than over counting anyway.
'''

from scripts import ARTICLES_FOLDER
import os, re

last_name = "melville"
full_name = "herman melville"

last_name_regex = re.compile(r"\b" + re.escape(last_name) + r"\b")
full_name_regex = re.compile(r"\b" + re.escape(full_name) + r"\b")

last_name_present = set()
full_name_present = set()

fnames = os.listdir(ARTICLES_FOLDER)

for fname in fnames:
    if "DS_Store" in fname:
        continue
    
    # get content
    with open(ARTICLES_FOLDER + fname, 'r') as fd:
        content = fd.read()

    if re.search(last_name_regex, content):
        last_name_present.add(fname)
        if re.search(full_name_regex, content):
            full_name_present.add(fname)

# get elements from set last_name_present which are not in full_name_present
diff_set = last_name_present - full_name_present

# print out data
print ("articles with \"" + last_name + "\" present: " + ','.join(last_name_present))
print ("articles with \"" + full_name + "\" present: " + ','.join(full_name_present))
print ("articles with \"" + last_name + "\" present but not \"" + full_name + "\": " + ','.join(last_name_present - full_name_present))

print ("# articles with \"" + last_name + "\" present: " + str(len(last_name_present)))
print ("# articles with \"" + full_name + "\" present: " + str(len(full_name_present)))
print ("# articles with \"" + last_name + "\" present but not \"" + full_name + "\": " + str(len(diff_set)))