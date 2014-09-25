'''
Created on Jun 24, 2014

@author: dbhage

Helper script to import data in mallet and run mallet topic modeller on the data.
'''

import subprocess

def import_data(mallet_folder, data_folder, mallet_file, stopwords_file):
    '''
    Import data into a .mallet file
    @param mallet_folder: folder where mallet is installed, containing a "bin" sub-folder
    @param data_folder: folder where your data files are present
    @param mallet_file: file in which to output the imported data
    @param stopwords_file: file containing stop-words, each on one line
    @precondition: assuming data folder is structured in a format provided by mallet
    '''
    if ' ' in mallet_folder or ' ' in data_folder:
        raise Exception("Folder names should not have any spaces.")
        
    import_command = mallet_folder + "bin/mallet import-dir --input " + data_folder + " --output " + mallet_file + " --keep-sequence --stoplist-file " + stopwords_file
    print ("Executing: " + import_command + '\n')
    subprocess.call(import_command.split())

def topic_model(mallet_folder, mallet_file, no_of_topics, keys_file_name, composition_file_name):
    '''
    Import data into a .mallet file
    @param mallet_folder: folder where mallet is installed, containing a "bin" sub-folder
    @param mallet_file: file in which to output the imported data
    @param no_of_topics: number of topics 
    @param keys_file_name: file name for file in which topics will be output in
    @param composition_file_name: file name for file in which article topic compositions will be stored
    @precondition: assuming data has already been imported in mallet_file
    '''
    if ' ' in mallet_folder:
        raise Exception("Folder names should not have any spaces.")

    topic_model_command = mallet_folder + "bin/mallet train-topics --input " + mallet_file + " --num-topics " + str(no_of_topics) + " --output-state topic-state.gz --output-topic-keys " + keys_file_name + " --output-doc-topics " + composition_file_name
    print ("Executing: " + topic_model_command + '\n')
    subprocess.call(topic_model_command.split())