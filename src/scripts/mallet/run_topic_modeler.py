'''
Created on Sep 25, 2014

@author: dbhage

Script to import data and run topic modeler
'''

from mallet.mallet import import_data,topic_model

mallet_folder = "PATH TO WHERE MALLET FOLDER IS INSTALLED"
data_folder = "PATH TO DATA FOLDER"
mallet_file = "FILE NAME FOR FILE IN WHICH MALLET WILL STORE .mallet FILE ONCE ITS IMPORTED"
stopwords_file = "FILE NAME FOR STOP WORDS"

import_data(mallet_folder, data_folder, mallet_file, stopwords_file)

no_of_topics = -1 # PLACE NUMBER OF TOPICS HERE
keys_file_name = "OUTPUT PATH/keys.txt"
composition_file_name = "OUTPUT PATH/compositions.txt"

topic_model(mallet_folder, mallet_file, no_of_topics, keys_file_name, composition_file_name)