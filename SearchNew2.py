import tweepy
import csv

#Twitter API information
consumer_key = "gsD8iFLqvQDdg22OFAHIhcIx9"
consumer_secret = "AiNjNSFUXwFRcD5CxFhrNhTNhrBm7ggznhSBhUIiDeXpChw07h"
access_key = "867029806944309254-Au0d3L1PpESXyyVSjGrqWBUdPOJspIC"
access_secret = "KRV42V1w9gHBlI4gxMSMtCEVZIp8CFpIG3HmKYT88P7FF"

#Authentication Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def search_func(value):
    search_results = api.search(q=value, count=10)

    outtweets_id = [result.id for result in search_results]

    length = len(outtweets_id)

    tweet_users = []

    for i in range(0, length):
        #if we retweeted a tweet that someone else retweeted then use retweeted_status
        #else just use the regular tweet result
        if search_results[i].retweeted_status is not None:
            tweet_users.append(search_results[i].retweeted_status.user)
        else:
            #regular user just get search results.user.screen_name
            tweet_users.append(search_results[i].user)
        try:
            api.retweet(outtweets_id[i])                #retweet the tweet
            print(tweet_users[i].screen_name)
        except Exception:
            pass
        
        #if 'follow' is in the tweet, follow that user, of course fails if
        #the word 'follow' is there for other reasons or the tweet uses more letters
        #in 'follow' i.e. 'follllllowww'
        if 'FOLLOW' in (search_results[i].text.upper()):
            api.create_friendship(tweet_users[i].id)
            

search_func("giveaway retweet")