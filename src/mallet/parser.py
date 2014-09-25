'''
Created on Sep 23, 2014

@author: dbhage

Module to parse mallet generated files into another format
'''

def keys_to_csv(keys, csv_file_name):
    '''
    Write keys as csv
    @param keys: list of Key objects
    @param csv_file_name: file in which to output data 
    '''
    with open(csv_file_name, 'w') as fd:
        fd.write("topic no,words\n")
        for key in keys:
            fd.write(str(key.topic_no) + ',' + ' '.join(key.words) + '\n')

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