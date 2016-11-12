import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'ZZHlgZYoCR72HWvqZ4LbFMNcb'
consumer_secret = 'Gx2g9Z5DwaBI3Bq0JyxK5pAwwPWqSdN4t1rf5mhghEhwMXGjzm'
access_token = '3320969365-Epm7HFGVOuPYKScLJYOpT9sMJMJHl1NvpNEnhn0'
access_secret = '7saqiEs5O6slpaqdXbJEZ9BAtRcI3HVceqWTUAEKslcRc'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.get_user('RuesgaSkyler')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)

# print('x')
# raise TypeError