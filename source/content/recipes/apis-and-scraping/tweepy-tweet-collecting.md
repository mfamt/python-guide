

A toolkit of things:


### An authentication function

Let's set up an Authentication file:

In: `.tweepy.json`

~~~json
[
  {
    "screen_name": "YOUR_SCREEN_NAME",
    "consumer_key": "CONSUMER_KEY",
    "consumer_secret": "CONSUMER_SECRET",
    "access_token": "ACCESS_TOKEN",
    "access_token_secret": "ACCESS_TOKEN_SECRET"
  }
]  
~~~


### Authenticating using your credentials

~~~py
import json
import os
import tweepy
import random
DEFAULT_TWITTER_CREDS_PATH = '~/.tweepy.json'

def open_creds_file(path = None):
    """
    opens a JSON file
    returns a List
    """
    if not path:
        path = DEFAULT_TWITTER_CREDS_PATH    # point to default file
    # get the full path to the file
    creds_fname = os.path.expanduser(path)
    # parse the JSON and load it as an Array
    creds = json.load(open(creds_fname))    
    return creds

def get_credentials(screen_name = None, creds_path = None):
    """
    returns a Dict
    """    
    creds = open_creds_file(path = creds_path)
    if screen_name:
        c = next(c for c in creds if c['screen_name'] == screen_name)
        return c
    else:
        # return a random credential
        random.shuffle(creds)
        return creds[0]


def get_api_client(screen_name = None, creds_path = None):
    """
    returns: a Tweepy object
    """
    creds = get_credentials(screen_name = screen_name, creds_path = creds_path)
    auth = tweepy.OAuthHandler(
      consumer_key = creds['consumer_key'], 
      consumer_secret = creds['consumer_secret'])
    auth.set_access_token(
      creds['access_token'], 
      creds['access_token_secret'])
    # create an API handler
    api = tweepy.API(auth) 
    return api


def get_user_timeline(screen_name, client = None):
    api = get_api_client() if client == None else client
    tweets = []
    cursor = tweepy.Cursor(api.user_timeline, id = screen_name, 
      trim_user = True, exclude_replies = False, include_rts = True)
    for tweet in cursor.items():
        tweets.append(tweet._json)

    return tweets




# sample use case:
replies = [t for t in tweets if t['in_reply_to_status_id']]

~~~




credsfile = os.path.expanduser('~/.tweepyrc')
creds = json.load(open(credsfile))
# Get authentication token
auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'], 
  consumer_secret = creds['consumer_secret'])
auth.set_access_token(creds['access_token'], 
  creds['access_token_secret'])
# create an API handler
api = tweepy.API(auth) 

print(type(api))           # <class 'tweepy.api.API'>
# get latest 20 tweets from your own timeline
home_tweets = api.home_timeline()
print(type(home_tweets))   # <class 'tweepy.models.ResultSet'>
print(len(home_tweets))    # 20 
~~~


~~~py
api = tweepy.API(auth) 
~~~



