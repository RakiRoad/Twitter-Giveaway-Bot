#=============================================================================
#   Twitter Bot that automatically enters user to giveaways
#   Created By: Ralph Quinto and Steve Mattia
#   Version: 1.0
#=============================================================================
#=============================================================================
#   Features to be implemented:
#
#
#   Major Issues:
#
#
#   Twitter account information
#
#=============================================================================
#import libraries
import tweepy
import csv
import threading
import time
import random

#Twitter API information
consumer_key = 	"CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"

#Authentication Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#//////////////////////////////////////////////////////////////////////////////
# Function to Retweet, Like, and Follow Giveaway
#//////////////////////////////////////////////////////////////////////////////

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

#//////////////////////////////////////////////////////////////////////////////
# Method to unfollow, delete tweets, and unlike
#//////////////////////////////////////////////////////////////////////////////

def undo_follow():

    #unfollows all of your friends
    for friends in tweepy.Cursor(api.friends).items():
        print ("Removing Follows...")
        try:
            api.destroy_friendship(friends.id)
        except:
            print ("Failed to unfollow")

def undo_retweets():

    #Deletes all of the retweets
    for retweets in tweepy.Cursor(api.user_timeline).items():
        print ("Removing Retweets...")
        try:
            api.destroy_status(retweets.id)
        except:
            print ("Failed to delete:")

def undo_favorites():

    #undoes all likes
    for retweets in tweepy.Cursor(api.favorites).items():
        print ("Removing Favorites...")
        try:
            api.destroy_favorite(retweets.id)
        except:
            print("Failed to unfavorite" + str(retweets.id))

#=================CODE TO RUN THE SCRIPT ========================


if __name__ == "__main__":

    for j in range (0, 5):
        for i in range (0, 10):
            print ("Passthrough: " + str(i+1) + " Loop: " + str(j+1))
            search_func("giveaway retweet", 150)
            time.sleep(60)

        randx = random.randint(15,35)
        if j < 5:
            print("Waiting " + str(randx) + " min...")
            time.sleep(60*randx)
        elif j == 5:
            print("Completed!")

    #=========UNCOMMENT TO UNFOLLOW, UNRETWEET, & UNFAVORITE ===========
    #undo_follow()
    #undo_retweets()
    #undo_favorites()