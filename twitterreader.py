import tweepy
import json
import mongo.py
from tweepy import OAuthHandler
from tweepy import Cursor
 
# access_token = '3320969365-Epm7HFGVOuPYKScLJYOpT9sMJMJHl1NvpNEnhn0'
# access_secret = '7saqiEs5O6slpaqdXbJEZ9BAtRcI3HVceqWTUAEKslcRc'

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
# api.update_status('@RuesgaSkyler tweepy + oauth!')

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.get_user('RuesgaSkyler')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)
