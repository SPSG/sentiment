from pymongo import MongoClient
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sid=SentimentIntensityAnalyzer()


# NLTK sentiment training data
#subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')]
#obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')]

#training_docs = [subj_docs] + [obj_docs]

#sentim_analyzer = SentimentAnalyzer()
#all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

#unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
#sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

#training_set = sentim_analyzer.aply_features(training_docs)

#trainer = NaiveBayesCLassifier.train
#classifier = sentim_analyzer.train(trainer, training_set)

# mongodb initialization/import
def dbload(dbname, collname):
    global client, db, tweets
    client = MongoClient()
    db = client[dbname]
    tweets = db[collname]



def score(tweets):
    for tweet in tweets.find():
        id = tweet['_id']
        scores=sid.polarity_scores(tweet['text'])
        tweets.update_one({'_id': id}, {'$set': {'sentiment_info': scores}})

if __name__ == '__main__':
    dbload('data', 'tweets')
    score(tweets)
        
