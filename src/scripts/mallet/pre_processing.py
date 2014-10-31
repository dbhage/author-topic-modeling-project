'''
Created on Oct 30, 2014

@author: dbhage

Script to preprocess corpus before using mallet topic modeler.

Requires pycelex-phonology (https://github.com/dbhage/pycelex-phonology)
'''

import os, sys
from scripts import ARTICLES_MAIN_DIR as ARTICLES_FOLDER, DROPBOX_FOLDER
from celex.factory.factory import build_celex

def expand_file(fname, english_words):
    '''
    Expand csv file with words and counts into words only
    
    @param fname: absolute path for file
    @type fname: str
    
    @param english_words: all english words
    @type english_words: iterable
    
    @return: text with expanded words and set of non eng words found in that file, None if file could not be read
    @rtype: (str, set<str>)
    '''
    current_non_english_words = set()
    
    try:
        text = ""
        
        with open(fname, 'r') as fd:
            lines = fd.readlines()
        
            for line in lines[1:]:
                line = line.replace('\n', '')
                line = line.split(',')
                
                bigram = line[0].split()
                
                # get the words in the bigram
                # only those words which are in the english words dictionary will be output
                # add non-english words to the current non english words set
                
                for word in bigram:
                    word = word.lower()
                    if word in english_words:
                        text += (word + ' ') * int(line[1])
                    else:
                        current_non_english_words.add(word)
                
        return (text, current_non_english_words)
    
    except IOError:
        print >> sys.stderr, "IOError while reading file: " + fname
        return None


# get the dictionary
english_words = build_celex(DROPBOX_FOLDER + "celex2/", 0, 0)

non_english_words = set()

# expand corpus files
for filee in sorted(os.listdir(ARTICLES_FOLDER + "bigrams/")):
    if not filee.endswith(".CSV"):
        continue
    
    fname = ARTICLES_FOLDER + "bigrams/" + filee

    print (fname)
    
    (text, current_non_eng_words) = expand_file(fname, english_words)
    non_english_words |= current_non_eng_words
    
    if text:
        with open(ARTICLES_FOLDER + "bigrams_expanded_eng_only/" + filee.replace(".CSV", '') + ".txt", 'w') as fd:
            fd.write(text)

# output non English words found
with open(ARTICLES_FOLDER + "non_eng_list_celex.csv", 'w') as fd:
    for word in sorted(non_english_words):
        fd.write(word + '\n')