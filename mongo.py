import twitterreader.py
from pymongo import MongoClient


#Make a connection to localhost
connection = MongoClient()

#initialize and assign collection
db = connection.data

#dump all tweets into db.tweets collection
def process_tweet(tweet):
	db.tweets.insert_many(json.dumps(tweet))

#sorts tweets from oldest to newest
timeline = db.tweets.find({}).sort({created_at: 1}) 

#obtain one document where its an original tweet
user = db.tweets.findOne({retweet: false})["author"]

#get all tweets that aren't quoted or retweeted
tweets = db.tweets.find({is_quote_status: false, retweeted: false, })

#gets all retweeted tweets
retweets = db.tweets.find({retweeted: true})

#creates a dictionary of tweet id strings as keys and number of favorites as values
fav_dict = {}
def favorites(tweet):
	for t in tweet:
		fav_dict[t["id_str"]] = t["favorite_count"]

favorites(timeline)


db.tweets.find().pretty()



#db.tweets.drop()


