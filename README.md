# Twitter-Giveaway-Scraper

![](https://img.shields.io/badge/Language-Python-brightgreen.svg) ![](https://img.shields.io/badge/Release-V1.1-blue.svg) ![](https://img.shields.io/badge/License-MIT-yellow.svg)

This Python script automatically enters users to giveaways by searching for the query terms "giveaway" and "retweet". This project was inspired by a Reddit post created a while back detailing a script that also entered the user to giveaways on Twitter. Seeing upon how successful the user was at winning, I decided to create my own version using Python and the Tweepy package.

## Features
- Automatically Enter User to Giveaways
- Undo Follow function
- Undo Retweet function
- Undo Favorite function
- Tag friends if specified in giveaways

## Requirements
- Python 3.0+
- Tweepy
- Twitter API Credentials

## Installation
1. Clone or download the repository
2. Open "bot.py" and replace placeholder text for API creditials with your generated keys for twitter
```python
#Twitter API information
consumer_key = 	"CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"
```
3. The script will automatically terminate after it operates through 7500 tweets
## Usage
**To run giveaway:**
1. Edit query term to search for or leave the default 'giveaway retweet'
2. Open Terminal and CD into repository directory
3. Type *python bot.py*
4. Operation ends after it operates through 7500 tweets

**To run the "un" functions:**
1. Comment out all the code within the nested for loops
2. Uncomment
```python
#undo_follow()
#undo_retweets()
#undo_favorites()
```
3. Open Terminal and CD into repository directory
4. Type *python bot.py*

```python
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
```

## Bugs/Limitations
1. There is currently a max follow limit of 5000. Once that cap is reached, account must unfollow all accounts listed under 'following'.
2. There is a cap of 1000 follows per day. Must unfollow if cap is reached

## Future Features
1. Automate unfollow when cap limit is reached.

## License

All source code in this app is released under the MIT license. See LICENSE for details. 
