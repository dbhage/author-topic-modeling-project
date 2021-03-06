'''
Created on Sep 15, 2014

@author: dbhage

Hard coded file or folder names to be used in the scripts. 

Keep all paths here so that when we run on different corpora, we don't need
to modify the scripts.
'''

ARTICLES_MAIN_DIR = "/Volumes/New HD/data/Lang_Lit_Lang_Lit_Bigrams/"

ARTICLES_FOLDER = ARTICLES_MAIN_DIR + "bigrams_expanded/"

HOME = False

if HOME:
    DROPBOX_FOLDER = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/"
else:
    DROPBOX_FOLDER = "/Volumes/Macintosh HD 2/Dropbox/PiperLabDeanSharedFolder/"

AUTHOR_NODE_LIST_FOLDER = DROPBOX_FOLDER + "TopicModels/authors/list/"

AUTHOR_MASTER_LIST_CSV_FNAME = DROPBOX_FOLDER + "TopicModels/BigramRecall/all_authors.csv"

AA_BIGRAM_VALIDATION_FILE = DROPBOX_FOLDER + "TopicModels/BigramRecall/Validation.csv"

GALENET_AUTHOR_MASTER_LIST_FNAME = AUTHOR_NODE_LIST_FOLDER + "galenet_author_master_list.txt"

UPPER_WORKING_FOLDER = DROPBOX_FOLDER + "TopicModels/Trial 8/"

CITATIONS_FILE_FNAME = UPPER_WORKING_FOLDER + "citations.csv"

JOURNAL_LIST_FILE_NAME = UPPER_WORKING_FOLDER + "journal_list.txt"

FOREIGN_TOPIC_REMOVE_CSV_FNAME = UPPER_WORKING_FOLDER + "foreign_topics_remove.csv"

WORKING_DIR = UPPER_WORKING_FOLDER + "all/"

ORIGINAL_COMPOSITIONS_FNAME = WORKING_DIR + "compositions.txt"

COMPOSITIONS_FNAME = WORKING_DIR + "compositions.txt"

AUTHOR_ARTICLE_CSV_FNAME = WORKING_DIR + "author_articles.csv"

AUTHOR_ARTICLE_MOST_POPULAR_CSV_FNAME = UPPER_WORKING_FOLDER + "author_articles_most_populat_galenet.csv"

AUTHOR_ARTICLE_LNC_CSV_FNAME = UPPER_WORKING_FOLDER + "author_articles_last_name_counts.csv"

AUTHOR_ARTICLE_CSV_COPY_FNAME = WORKING_DIR + "author_articles_copy.csv"

ARTICLE_TOPIC_CSV_FNAME = WORKING_DIR + "article_topic.csv"

ENTROPIES_CSV_FNAME = WORKING_DIR + "entropies.csv"

COOCCURRENCE_LIST_FNAME = WORKING_DIR + "cooccurrence_list.csv"

AUTHOR_COOCCURRENCE_EDGE_LIST_PLUS10 = WORKING_DIR + "Author_Cooccurrence_EdgeList_Plus10.csv"

AUTHOR_DATE_CSV_FNAME = WORKING_DIR + "author_date.csv"

PURITIES_METADATA_FNAME = WORKING_DIR + "purities_metadata.txt"

PURITIES_CSV_FNAME = WORKING_DIR + "purities.csv"

PUBDATE_TOPIC_CSV_FNAME = WORKING_DIR + "pubdate_topic.csv"

AUTHOR_TOPIC_CSV_FNAME = WORKING_DIR + "author_topic_table.csv"

AUTHOR_TOPIC_BEAUTIFIED_FNAME = WORKING_DIR + "author_topic_better_representation.txt"

AUTHOR_TOPIC_TABLE_WITH_COUNTS_TABLE_FNAME = WORKING_DIR + "author_topic_table_with_counts.csv"

AUTHOR_TOPIC_COOCCURRENCE_LIST_FNAME = WORKING_DIR + "author_topic_cooccurrence_list.csv"

# sum, conns and percentages
NODE_FNAME = UPPER_WORKING_FOLDER + "Author_Topic_Nodelist.csv"

SUM_AND_CONNECTIONS_OUTPUT_FNAME = WORKING_DIR + "sum_and_connections.csv"

# keywords data subset by year
KEYWORDS_OUTPUT_FILE = UPPER_WORKING_FOLDER + "keywords.csv"

# article pubdate table
ARTICLE_PUBDATE_FNAME = UPPER_WORKING_FOLDER + "article_pubdate.csv"