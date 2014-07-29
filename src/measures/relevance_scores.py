'''
Created on Jul 22, 2014

@author: dbhage

Measure precision, recall and accuracy.
'''

def precision(tp, fp):
    '''
    Get the fraction of retrieved instances that are relevant
    @param tp: # true positives
    @param fp: # false positives
    @return: precision as a float
    '''
    return tp / float(tp + fp)

def recall(tp, fn):
    '''
    Get fraction of relevant instances that are retrieved
    @param tp: # true positives
    @param fn: # false negatives
    @return: recall as a float
    '''
    return tp / float(tp + fn)

def accuracy(tp, tn, fp, fn):
    '''
    Calculate accuracy
    @param tp: # true positives
    @param fp: # false positives
    @param fn: # false negatives
    @param tn: # true negatives
    @return: accuracy as a float
    '''
    return (tp + tn) / float(tp + tn + fp + fn)