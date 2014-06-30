'''
Created on Jun 26, 2014

@author: dbhage

Module to expand corpus with <word, word count> as lines in files.
'''

import os, sys

def expand_file(fname):
    '''
    Expand csv file with words and counts into words only
    '''
    try:
        text = ""
        with open(fname, 'r') as fd:
            lines = fd.readlines()
            for line in lines[1:]:
                line = line.replace('\n', '')
                line = line.split(',')
                text += (line[0] + ' ') * int(line[1])
        return text
    except IOError:
        print >> sys.stderr, "IOError while reading file: " + fname
        return None

def expand_jstor_corpus(n):
    '''
    Take n word count files from JSTOR corpus and produce a text file with the words
    '''
    jstor_folder = "/home/dbhage/piperlab/JSTORAllLang&Lit1950-2008/JSTORData-09.2012/"
    for filee in os.listdir(jstor_folder + "wordcounts/")[:n]:
        if filee.endswith(".CSV"):
            fname = jstor_folder + "wordcounts/" + filee
            print (fname)
            text = expand_file(fname)
            if text:
                with open(jstor_folder + "wordcounts_reduced/" + filee.replace(".CSV", '') + ".txt", 'w') as fd:
                    fd.write(text)

def expand_smaller_jstor_corpus():
    jstor_folder = "/Volumes/Macintosh HD 2/corpus/disciplinarity/JSTOR_MultiDiscipline/Languages_Literatures_Subset_LangLit_Dataset/"
    for filee in os.listdir(jstor_folder + "wordcounts/"):
        if filee.endswith(".CSV"):
            fname = jstor_folder + "wordcounts/" + filee
        else:
            continue
        print (fname)
        text = expand_file(fname)
        if text:
            with open(jstor_folder + "wordcounts_expanded/" + filee.replace(".CSV", '') + ".txt", 'w') as fd:
                fd.write(text)