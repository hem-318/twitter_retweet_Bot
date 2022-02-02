from random import randint
#You can set your preferences here,

# Edit this config.py file as you like

# This is hastag which Twitter bot will search for and retweet 
from random import randint
QUERY = '#keyword'

#Set this to true if you want to enable like+retweet 
LIKE = False

#Enable this if you want to follow the user whose tweet has been retweetec
FOLLOW = False

#To specify the amount of time it needs to wait between 2 consecutive retweets
#I've randomized it between 30-45 seconds wait.This will prevent api from getting limits
SLEEP_TIME = randint(30,45)
