'''
Created on Jul 16, 2014

@author: dbhage

Module to measure author name recognition accuracy
'''

import re

def anr_accuracy(validated_data, generated_data):
    '''
    Measure Author Name Recognition Accuracy, ignoring the significance of the author's presence
    @param validated_data: dict with article id as key and ArticleAuthorContent object as key
    @param generated_data: dict with article name as key and list of authors present in that article as value
    '''
    
    if validated_data is None or generated_data is None:
        return None

    # TODO: implement

    raise Exception("Not yet implemented")
    
def anr_comparison_string(validated_data, generated_data):
    '''
    Get generated versus validated author name recognition comparison string
    @param validated_data: dict with article id as key and ArticleAuthorContent object as key
    @param generated_data: dict with article name as key and list of authors present in that article as value
    '''
    output_string = "aid, generated, validated\n"
    
    for (article_id, article_author_content) in validated_data.items():
        generated_authors = generated_data["wordcounts_10.2307_" + str(article_id) + ".txt"]
        validated_authors = article_author_content.get_author_list()
        
        output_string += str(article_id) + ','
        
        for ga in generated_authors:
            output_string += str(ga) + ';'

        output_string += ','
        
        for va in validated_authors:
            output_string += str(va) + ';'
        
        output_string += '\n'
    
    return output_string

def get_validated_data(lines):
    if lines is None or lines == []:
        return None
    
    validated_data = dict()
    
    for line in lines:
        line = line.split(',')
        
        try:
            aid = int(line[0])
        except ValueError:
            continue
        
        mention = line[1].lower()
        mention = ' '.join(re.findall(r"[a-zA-Z]+", mention))

        if re.search("yes", line[2], re.I):
            significant = True
        else:
            significant = False

        if aid not in validated_data:
            article_author_content = ArticleAuthorContent(aid)
            validated_data[aid] = article_author_content
        
        validated_data[aid].add_mention(mention, significant)
    
    return validated_data

class ArticleAuthorContent(object):
    '''
    Data structure to keep authors mentioned in articles and the significance of the author's presence
    '''
    def __init__(self, aid):
        '''
        @param aid: integer representing the article id
        '''
        if (not aid is None) and aid > 0:
            self.article_id = aid
            self.mentions = dict()
        else:
            raise ValueError("article id should be an integer >= 0")
    
    def add_mention(self, author, significant):
        '''
        Add a mentioned author and the significance of the mention
        @param author: string representing author's name
        @param significant: bool which is True if mention is significant, False otherwise
        @precondition: self.mentions must have been initialized
        '''
        if author not in self.mentions:
            self.mentions[author] = significant
        else:
            if self.mentions[author] != significant:
                raise ValueError("Trying to add author \"" + str(author) + "\" to mentions. Author already present with another significance.")
    
    def get_author_list(self):
        '''
        @return: return a list of all authors mentioned in this article
        '''
        return self.mentions.keys()
    
    def get_significant_author_list(self):
        '''
        @return: return a list of all SIGNIFICANT authors mentioned in this article
        '''
        return [k for k in self.mentions.keys() if self.mentions[k]]
        