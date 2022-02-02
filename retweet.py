import tweepy
from time import sleep
from keys import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

print("Twitter bot which retweets, like tweets and follow users")
print("Bot config")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search_tweets, q = QUERY).items():
	try:
		print('\nTweet by: @' + tweet.user.screen_name)

		tweet.retweet()
		print('Retweeted the tweet')

		# Favorite the tweet
		if LIKE:
			tweet.favorite()
			print('Liked the tweet')

		# Follow the user who tweeted
		# check that bot is not already following the user
		if FOLLOW:
			if not tweet.user.following:
				tweet.user.follow()
				print('Followed the user')

		sleep(SLEEP_TIME)

	except tweepy.errors.Forbidden as e:
		print (e)

	except tweepy.errors.TooManyRequests as f:
		print (f)

	except StopIteration:
		break
#Code by Hem (icecracker_hem on twitter)
