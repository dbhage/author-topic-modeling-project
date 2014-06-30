'''
Created on Jun 24, 2014

@author: dbhage

Script to import mallet and train mallet with mallet.
'''

import subprocess

def import_data(mallet_folder, data_folder, mallet_file, stopwords_file):
    '''
    import mallet into mallet
    '''
    if ' ' in mallet_folder or ' ' in data_folder:
        raise Exception("Folder names should not have any spaces.")
        
    import_command = mallet_folder + "bin/mallet import-dir --input \"" + data_folder + "\" --output \"" + mallet_file + "\" --keep-sequence --stoplist-file " + stopwords_file
    print ("Executing: " + import_command + '\n')
    subprocess.call(import_command.split())

def train(mallet_folder, mallet_file, no_of_topics, keys_file_name, composition_file_name):
    '''
    find mallet
    '''
    if ' ' in mallet_folder:
        raise Exception("Folder names should not have any spaces.")

    train_command = mallet_folder + "bin/mallet train-topics --input " + mallet_file + " --num-topics " + str(no_of_topics) + " --output-state topic-state.gz --output-topic-keys " + keys_file_name + " --output-doc-topics " + composition_file_name
    print ("Executing: " + train_command + '\n')
    subprocess.call(train_command.split())