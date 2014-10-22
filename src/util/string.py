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
    
    @param text: text
    @type text: str
    
    @return: text with uhmlauts
    @rtype: str
    '''
    text = text.decode('utf-8')
    text = text.replace(unichr(252), 'ue') # 252 corresponds to u-umlaut
    text = text.replace(unichr(246), 'oe') # 246 corresponds to o-umlaut
    text = text.replace(unichr(228), 'ae') # 228 corresponds to a-umlaut
    text = text.replace(unichr(223), 'ss') # 223 corresponds to that beta looking thingy
    text = text.encode('utf-8')
    text = text.replace('\'', '')
    return text

def get_longest_string(str_list):
    '''
    Get the longest string in list
    
    @param str_list: list of strings
    @type str_list: list str
    
    @return: longest string in str_list
    @rtype: str
    
    @raise ValueError: if parameter invalid
    '''
    if not str_list:
        raise ValueError("string list invalid")
    
    longest = ""
    for element in str_list:
        if (len(element) > len(longest)):
            longest = element
    return longest