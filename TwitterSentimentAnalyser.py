import tweepy
from textblob import TextBlob

# Enter you keys by signing up at https://apps.twitter.com
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret =  ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

pos=0
neg=0
neutral=0

public_tweets = api.search('Modi',show_user=[True])

for tweet in public_tweets:
	if (not tweet.retweeted) and ('RT @' not in tweet.text):
		print (tweet.user.name + ':' + tweet.text)
		analysis = TextBlob(tweet.text)
		print (analysis.sentiment.polarity)
		polarity_value = analysis.sentiment.polarity
		if polarity_value > 0:
			pos+=1
		elif polarity_value < 0:
			neg+=1
		else:
			neutral+=1
print (pos,neg,neutral)