import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Cursor
from pymongo import MongoClient
from pprint import pprint
 
# access_token = '3320969365-Epm7HFGVOuPYKScLJYOpT9sMJMJHl1NvpNEnhn0'
# access_secret = '7saqiEs5O6slpaqdXbJEZ9BAtRcI3HVceqWTUAEKslcRc'

#Make a connection to localhost
connection = MongoClient()

#initialize and assign collection
db = connection.data

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

def get_twitter_bot():
	consumer_key = 'ZZHlgZYoCR72HWvqZ4LbFMNcb'
	consumer_secret = 'Gx2g9Z5DwaBI3Bq0JyxK5pAwwPWqSdN4t1rf5mhghEhwMXGjzm'
	key = '3320969365-Epm7HFGVOuPYKScLJYOpT9sMJMJHl1NvpNEnhn0'
	secret = '7saqiEs5O6slpaqdXbJEZ9BAtRcI3HVceqWTUAEKslcRc'
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(key, secret)
	return auth

def get_twitter_client(auth): #pass in the authentication testing or user specific
	client = tweepy.API(auth) 
	return client

def get_user_timeline():
	# change the line below to reflect whether testing or not
	client = get_twitter_client(get_twitter_bot()) 
	for tweet in tweepy.Cursor(client.user_timeline).items():
		db.tweets.insert(tweet._json)


get_user_timeline()

#sorts tweets from oldest to newest
timeline = db.tweets.find({'retweeted': False}).sort('created_at', 1)

#obtain one document where its an original tweet
user_cursor = db.tweets.find_one({'retweeted': False})
#if user_cursor:
#	user_cursor = user_cursor['user']['name']

#get all tweets that aren't quoted or retweeted
tweets_cursor = db.tweets.find({'is_quote_status': False, 'retweeted': False, })

#gets all retweeted tweets
retweets_cursor = db.tweets.find({'retweeted': True})

#

#creates a dictionary of tweet id strings as keys and number of favorites as values
fav_dict = {}
def favorites(tweet):
	for t in tweet:
		fav_dict[t["id_str"]] = t["favorite_count"]
	fav_dict['total_favs'] = sum(fav_dict.values())
	fav_dict['total_posts'] = len(fav_dict) - 1
	fav_dict['fav_ratio'] = fav_dict['total_favs'] / fav_dict['total_posts']
favorites(timeline)

pprint(user_cursor)
