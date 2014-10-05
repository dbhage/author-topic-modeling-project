'''
Created on Sep 23, 2014

@author: dbhage

Module to parse mallet generated files into another format
'''

def keys_to_csv(keys, csv_file_name):
    '''
    Write keys as csv where a row is a topic number followed by its words
    @param keys: list of Key objects
    @param csv_file_name: file in which to output data 
    '''
    with open(csv_file_name, 'w') as fd:
        for key in keys:
            fd.write(str(key.topic_no) + ',' + ','.join(key.words) + '\n')

def keys_to_csv1(keys, csv_file_name):
    '''
    Write keys as csv where a column in a topic number followed by its words
    this would output the transpose of keys_to_csv
    @param keys: list of Key objects
    @param csv_file_name: file in which to output data 
    '''
    with open(csv_file_name, 'w') as fd:
        fd.write(','.join([str(k.topic_no) for k in keys]) + '\n')
        for i in range(0, len(keys[0].words)):
            for k in keys:
                fd.write(k.words[i] + ',')
            fd.write('\n')
            
def document_topic_matrix(compositions, no_of_topics, csv_file_name):
    '''
    Produce a document-topic matrix with topic proportions as values
    @param compositions: dict with document name as key and Composition object as value 
    @param no_of_topics: 150
    @param csv_file_name: file in which to output data
    '''
    with open(csv_file_name, 'w') as fd:
        fd.write(',' + ','.join(str(i) for i in range(0, no_of_topics)) + '\n')
        for (doc, compo) in compositions.items():
            fd.write(doc.replace(',', '$') + ',')
            for i in range(0, no_of_topics):
                try:
                    topic_proportion = compo.topic_proportions[i]
                    fd.write(str(topic_proportion) + ',')
                except KeyError:
                    fd.write("0,")
            fd.write('\n')    