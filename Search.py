#import stuff

import tweepy
import csv

#Twitter API information
consumer_key = "gsD8iFLqvQDdg22OFAHIhcIx9"
consumer_secret = "AiNjNSFUXwFRcD5CxFhrNhTNhrBm7ggznhSBhUIiDeXpChw07h"
access_key = "867029806944309254-Au0d3L1PpESXyyVSjGrqWBUdPOJspIC"
access_secret = "KRV42V1w9gHBlI4gxMSMtCEVZIp8CFpIG3HmKYT88P7FF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def search_func(value):
	results = api.search(q=value)
	#for result in results:
		#print (result)
	outtweets = [[result.text.encode("utf-8")] for result in results]

    # write the csv
	with open('%s_tweets.csv' % value, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["text"])
		writer.writerows(outtweets)
	pass

search_func("giveaway")