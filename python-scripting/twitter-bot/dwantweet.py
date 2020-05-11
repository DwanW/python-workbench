# note this app follows back followers and favorite 1 tweet that contains the keyword python
import tweepy
import time

auth = tweepy.OAuthHandler('JPL62OeeTpSRyVq6dpGEPqNIY', 'ZdCEVbo9Gl3MArzpQ9jGJ1NrngntH2Il9dgFCdmAbraeEgoIKz')
auth.set_access_token('1259897541413371904-MpxXUiyTjHMMHFbnRpEdiVi2cW7nAf', 'HfQa5dQ2VZz1C2ti0QN9NmFTlZUbJ8FrngfI7ksiLQ7Pq')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            try:
                yield cursor.next()
            except StopIteration:
                return
    except tweepy.RateLimitError:
        time.sleep(1000)

#Generous Bot that follows back
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    try:
        follower.follow()
    except tweepy.RateLimitError:
        time.sleep(1000)

# Narcissist Bot that follows back
search_string = 'python'
numbersOfTweets = 1

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)