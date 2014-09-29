'''
Created on Jun 30, 2014

@author: dbhage

String utility functions
'''

def to_lower(word): 
    return word.lower()

def replace_uhmlauts(text):
    '''
    Replace umhlauts in german text
    '''
    text = text.decode('utf-8')
    text = text.replace(unichr(252), 'ue') # 252 corresponds to u-umlaut
    text = text.replace(unichr(246), 'oe') # 246 corresponds to o-umlaut
    text = text.replace(unichr(228), 'ae') # 228 corresponds to a-umlaut
    text = text.replace(unichr(223), 'ss') # 223 corresponds to that beta looking thingy
    text = text.encode('utf-8')
    text = text.replace('\'', '')
    return text