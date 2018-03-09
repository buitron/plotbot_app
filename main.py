import tweepy, os, time, csv
from daft_punky import Twitter_Checker, Twitter_Validator, Twitter_Plotter

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    time.sleep(60 * 5)
    trash_it = Twitter_Validator(api)
    change_it = Twitter_Checker(api)

    mail_upgrade_it = trash_it.check_request()

    if mail_upgrade_it:
        screen_name, user_name, tweet_id = change_it.search_request()
        if screen_name:
            success = Twitter_Plotter(api, screen_name, user_name, tweet_id)
            success.send_it()
