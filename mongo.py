import twitterreader.py
from pymongo import MongoClient


#Make a connection to localhost
connection = MongoClient()

#initialize and assign collection
db = connection.data

def process_tweet(tweet):
	db.tweets.insert_many(json.dumps(tweet))


timeline = db.tweets.find({}).sort({created_at: 1}) 


#obtain one document where its an original tweet
user = db.tweets.findOne({retweet: false})["author"]

tweets = db.tweets.find({is_quote_status: false, retweeted: false, })

retweets = db.tweets.find({retweeted: true})

fav_dict = {}
def favorites(tweet):
	for t in tweet:
		fav_dict[t["id_str"]] = t["favorite_count"]

favorites(timeline)


db.tweets.find().pretty()



#db.tweets.drop()


