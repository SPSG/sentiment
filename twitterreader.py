import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Cursor
from pymongo import MongoClient
 
# access_token = '3320969365-Epm7HFGVOuPYKScLJYOpT9sMJMJHl1NvpNEnhn0'
# access_secret = '7saqiEs5O6slpaqdXbJEZ9BAtRcI3HVceqWTUAEKslcRc'


#Make a connection to localhost
connection = MongoClient()

#initialize and assign collection
db = connection.data

#dump all tweets into db.tweets collection
def process_tweet(tweet):
	db.tweets.insert(tweet)

	#sorts tweets from oldest to newest
	#timeline = db.tweets.find().sort({'created_at': 1})

	#obtain one document where its an original tweet
	user_cursor = db.tweets.find({'retweet': False})

	#get all tweets that aren't quoted or retweeted
	tweets_cursor = db.tweets.find({'is_quote_status': False, 'retweeted': False, })

	#gets all retweeted tweets
	retweets_cursor = db.tweets.find({'retweeted': True})

	#creates a dictionary of tweet id strings as keys and number of favorites as values
	#fav_dict = {}
	#def favorites(tweet):
	#	for t in tweet:
	#		fav_dict[t["id_str"]] = t["favorite_count"]

	#favorites(timeline)

	for user in user_cursor:
		print(user)


def get_twitter_auth():
	# Setup Twitter autentication
	consumer_key = 'ZZHlgZYoCR72HWvqZ4LbFMNcb'
	consumer_secret = 'Gx2g9Z5DwaBI3Bq0JyxK5pAwwPWqSdN4t1rf5mhghEhwMXGjzm'
	auth = OAuthHandler(consumer_key, consumer_secret)
	try:
		redirect_url = auth.get_authorization_url()
	except tweepy.TweepError:
		print('Error! Failed to get request token.')

	print(redirect_url)
	verifier = input('Verifier:')

	try:
		auth.get_access_token(verifier)
	except tweepy.TweepError:
		print('Error! Failed to get access token')

	key = auth.access_token
	secret = auth.access_token_secret
	auth.set_access_token(key, secret)
	return auth

def get_twitter_client():
	auth = get_twitter_auth() 
	client = tweepy.API(auth) 
	return client

def get_timeline():
	client = get_twitter_client() 
	for tweet in tweepy.Cursor(client.user_timeline).items():
		process_tweet(tweet._json)

get_timeline()



#db.tweets.drop()





# api.update_status('@RuesgaSkyler tweepy + oauth!')

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.get_user('RuesgaSkyler')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)
