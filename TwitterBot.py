#=============================================================================
#   Twitter Bot that automatically enters user to giveaways
#   Created By: Ralph Quinto and Steve Mattia
#   Version: 1.0
#=============================================================================
#import libraries
import tweepy
import csv
import threading

#Twitter API information
consumer_key = "wiC1ZB8wj6d6rGwhL9jMKDmLb"
consumer_secret = "ov5uyROCQZj4zVndtn39t1QHtCuDvBuS02SzvlIVQxlU9UhprY"
access_key = "867029806944309254-NmtVbhCbayOtWGO4kMpS8PrgfF5MRCY"
access_secret = "xKcFPqEbhmdoOHHAjDx8QJ6ODRld5o1PlC8K5Ss1BkDIz"

#Authentication Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


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


# def runSearchOnIntervalMinutes(query, minutes):
#     seconds = minutes * 60.0
#     threading.Timer(seconds, search_func).start()

# def runSearchOnIntervalSeconds(query, seconds):
#     threading.Timer(seconds, search_func).start()



#///////////////////////////////////////////////////////////
# Method to unfollow and delete tweets
#///////////////////////////////////////////////////////////

def undo_func():

    #Finds the owner's id
    me_user = api.me()
    me_id = me_user.id

    #print (me_id)
    #print ("\n")

    #finds the ids of followings
    following_list = api.friends_ids(me_id)
    #print (following_list)
    #print ("\n")
    length_follow = len(following_list)

    #iterates through the list of followings and deletes it
    for i in range(0, length_follow):
        api.destroy_friendship(following_list[i])
        #print ("Deleting " + str(following_list[i]))

    #Deletes all of the retweets and unlikes them
    for retweets in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(retweets.id)
            #print ("Deleted:"), retweets.id
        except:
            print ("Failed to delete:"), retweets.id

        if retweets.favorited:
            try:
                api.destroy_favorite(retweets.id)
            except Exception as e:
                print("Failed to unfavorite" + str(retweets.id))
                print(str(e.errno))

"""
Major Issues:

Features to be implemented:
	-We need to make the program keep searching for new giveaways so far only runs a single instance
	-Add functionality so program automatically retweets, follows, favorite tweet for giveaway
		-Does retweeting
		-Does Following

Twitter account information
	Email: redditfreebies28@gmail.com
	Password: Rockyisgod28
"""

'''
random idea

try to handle situation where tweets say "like: youtube.com/fdaf":
    if link contains 'youtube' or shortened version, go to youtube with account credentials and like (use youtube api/lib)

'''

#=================CODE TO RUN THE SCRIPT ========================
search_func("giveaway retweet", 50)
#undo_func()
