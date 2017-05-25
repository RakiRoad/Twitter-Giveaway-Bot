#=============================================================================
#   Twitter Bot that automatically enters user to giveaways
#   Created By: Ralph Quinto and Steve Mattia
#   Version: 1.0
#=============================================================================
#=============================================================================
#   Features to be implemented:
#       We need to make the program keep searching for new giveaways so far
#       only runs a single instance
#
#   Major Issues:
#       Rewrite the undo_follow function
#
#   Twitter account information
#	  Email: redditfreebies28@gmail.com
#	  Password: Rockyisgod28
#     user_id = 867029806944309254
#
#=============================================================================
#import libraries
import tweepy
import csv
import threading
import time
#Twitter API information
consumer_key = 	"SOkTAHoHprwL0numjECCApGVw"
consumer_secret = "44VWtmg0oBtq5u1rq97W4BvouKrOkQPaienHm3LsmqdXVgJs05"
access_key = "867029806944309254-PRCyOXnVmRel0KFFW27eB0Gdg3I3BXo"
access_secret = "uvC513O208HRLzOyFab5FRIt48o4ew30H5CB1YKlqKadT"

#Authentication Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def search_func(value, numTweets):
    search_results = api.search(q=value, count=numTweets)

    outtweets_id = [result.id for result in search_results]

    length = len(outtweets_id)

    tweet_users = []

    for i in range(0, length):
        #if we retweeted a tweet that someone else retweeted then use retweeted_status
        #else just use the regular tweet result
        if hasattr(search_results[i], 'retweeted_status'):
            tweet_users.append(search_results[i].retweeted_status.user)
        else:
            #regular user just get search results.user.screen_name
            tweet_users.append(search_results[i].user)
        try:
            api.retweet(outtweets_id[i])                #retweet the tweet
            #print(tweet_users[i].screen_name)
        except Exception:
            pass

        #if 'follow' is in the tweet, follow that user, of course fails if
        #the word 'follow' is there for other reasons or the tweet uses more letters
        #in 'follow' i.e. 'follllllowww'
        if 'FOLLOW' in (search_results[i].text.upper()):
            try:
                api.create_friendship(tweet_users[i].id)
            except Exception:
                pass

		#if 'like' is in the tweet, like that tweet, of course fails if
        #the word 'like' is there for other reasons or the tweet uses more letters
        #in 'like' i.e. 'liiiikee'
        if 'LIKE' in (search_results[i].text.upper()) or 'FAVORITE' in (search_results[i].text.upper()):
            try:
                api.create_favorite(outtweets_id[i])
            except Exception:
                pass

#///////////////////////////////////////////////////////////
# Method to unfollow, delete tweets, and unlike
#///////////////////////////////////////////////////////////

def undo_follow():

    for friends in tweepy.Cursor(api.friends).items():
        try:
            api.destroy_friendship(friends.id)
        except:
            print ("Failed to unfollow")

def undo_retweets():
    #Deletes all of the retweets
    for retweets in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(retweets.id)
            #print ("Deleted:"), retweets.id
        except:
            print ("Failed to delete:"), retweets.id

def undo_favorites():

    #undoes all likes
    for retweets in tweepy.Cursor(api.favorites).items():

        try:
            api.destroy_favorite(retweets.id)
        except Exception as e:
            print("Failed to unfavorite" + str(retweets.id))
            print(str(e.errno))

#=================CODE TO RUN THE SCRIPT ========================
#search_func("giveaway retweet", 5)
#undo_follow()
#undo_retweets()
#undo_favorites()
