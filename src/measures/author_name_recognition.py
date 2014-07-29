'''
Created on Jul 16, 2014

@author: dbhage

Module to measure author name recognition accuracy
'''

import re

from author.names import find_upper_lowers_pattern
from author.author import Author

def anr_accuracy(validated_data, generated_data, sig=False):
    '''
    Measure Author Name Recognition Accuracy, ignoring the significance of the author's presence
    @param validated_data: dict with article id as key and ArticleAuthorContent object as key
    @param generated_data: dict with article id as key and list of authors present in that article as value
    @param sig: use only significant authors if True, use all authors if False
    @return: string representing the matches
    '''
    
    raise Exception("NYI")
    
    # TODO: adapt to Author
    
    if validated_data is None or generated_data is None:
        return None
    
    return_string = ""
    
    true_positive_count = 0
    false_positive_count = 0
    
    for article_id in validated_data.keys():
        return_string += "article_id:" + str(article_id) + "\n"
        
        if sig:
            correct_authors = validated_data[article_id].get_significant_author_list()
        else:
            correct_authors = validated_data[article_id].get_author_list()
        
        generated_authors = generated_data[article_id]

        for gen_auth in generated_authors:
            gen_auth_last_names = gen_auth.last_names
            gen_auth_found = False

            for corr_auth in correct_authors:
                corr_auth_last_name = corr_auth.split()[-1]

                for gen_auth_last_name in gen_auth_last_names:

                    if gen_auth_last_name == corr_auth_last_name:
                        gen_auth_found = True
                        return_string += "\tmatch: gen:" + str(gen_auth) + " val:" + str(corr_auth) + '\n'
                        break

            if gen_auth_found:
                true_positive_count += 1
            else:
                false_positive_count += 1
                return_string += "\tNot Found:" + str(gen_auth) + '\n'
        
    return_string += "\ntp:" + str(true_positive_count) + ", fp:" + str(false_positive_count) + '\n'

    return return_string

def anr_comparison_string(validated_data, generated_data, sig=False):
    '''
    Get generated versus validated author name recognition comparison string
    @param validated_data: dict with article id as key and ArticleAuthorContent object as key
    @param generated_data: dict with article name as key and list of authors present in that article as value
    @param sig: use only significant authors if True, use all authors if False
    @return: string representing a table with article id, generated authors and validated authors
    '''
    output_string = "aid, generated, validated\n"
    
    for (article_id, article_author_content) in validated_data.items():
        generated_authors = generated_data[article_id]

        if sig:
            validated_authors = article_author_content.get_significant_author_list()
        else:
            validated_authors = article_author_content.get_author_list()
        
        output_string += str(article_id) + ','
        
        for ga in generated_authors:
            output_string += str(ga) + ';'

        output_string += ','
        
        for va in validated_authors:
            output_string += str(va) + ';'
        
        output_string += '\n'
    
    return output_string

def get_validated_data(lines, prepend_to_id="", append_to_id=""):
    '''
    Get the validated data
    @param lines: List of string representing lines of the validated data from the csv file
    @param prepend_to_id: any string which needs to be added at the beginning of the article id
    @param append_to_id: any string which needs to be added after the article id
    @return: dict with article id as key and ArticleAuthorContent object as value
    '''
    if lines is None or lines == []:
        return None
    
    validated_data = dict()
    
    for line in lines:
        line = line.split(',')
        
        try:
            aid = prepend_to_id + str(int(line[0])) + append_to_id
        except ValueError:
            continue

        mentions_last_names = find_upper_lowers_pattern(line[1])

        if mentions_last_names == []:
            raise ValueError("No last name found for author.\nLine:" + ','.join(line))
        
        mention_first_names = find_upper_lowers_pattern(line[2])
        
        mention = Author()
        
        mention.add_last_names(mentions_last_names)
        mention.add_first_names(mention_first_names)

        if re.search("yes", line[3], re.I):
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
        @param author: Author object
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