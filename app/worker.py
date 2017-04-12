import requests
import tweepy
import json
SOCIAL_MONITORING_API = 'http://127.0.0.1:5000'
TWEETER_CONSUMER_KEY = 'Z8YW5nSlbyr08IJsCVMlUcMsE'
TWEETER_CONSUMER_SECRET = 'DhSuQTNVw02Fenl4mx2dAu44rtTc45WlDXF38kW5YUgZpFWR2Q'
TWEETER_ACCESS_TOKEN = '817831349075767297-Zso7CMIJUdFKvIsF3w8ovA8eVEsOc9w'
TWEETER_ACCESS_TOKEN_SECRET = 'Phn0vUlqYI5Bm3yedkTtmMUW6LkwhUhyBHP2iHNiF3kTs'
auth = tweepy.OAuthHandler(TWEETER_CONSUMER_KEY, TWEETER_CONSUMER_SECRET)
auth.set_access_token(TWEETER_ACCESS_TOKEN, TWEETER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
SEARCH = ['sale']


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print json.dumps(status._json, indent=2)
       # add_tweet(status)


def process():
    myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
    myStream.filter(track=SEARCH)


def add_tweet(tweet):
    endpoint = 'http://{host}/tweets'.format(host=SOCIAL_MONITORING_API)
    response = requests.post(endpoint, json=tweet._json)
    if not response.ok:
        print 'Failed to save tweet:', response.text


def run():
    while True:
        try:
            print 'Start listening...'
            process()
        except KeyboardInterrupt:
            print 'Interrupted... Stopping worker.'
            return

if __name__ == '__main__':
    run()
