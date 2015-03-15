---
title: Introduction to Tweepy and the Twitter API
references:
  - url: http://tweepy.readthedocs.org/en/stable/
---

## Installation

~~~sh
pip install tweepy
~~~


## Set up a personal application




### Create a credentials file

In: `.tweepyrc`

~~~json
{
  "consumer_key": "CONSUMER_KEY",
  "consumer_secret": "CONSUMER_SECRET",
  "access_token": "ACCESS_TOKEN",
  "access_token_secret": "ACCESS_TOKSECRET"
}
~~~


## Hello Tweepy


### Authenticating using your credentials

~~~py
import json
credsfile = os.path.expanduser('~/.tweepyrc')
creds = json.load(open(credsfile))

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



### The `tweepy.models.Status` object

~~~py
tweet = home_tweets[0]
print(type(tweet))    #    <class 'tweepy.models.Status'>
~~~

### The `tweepy.models.User` object

~~~py
user = tweet.user
print(type(user))               # <class 'tweepy.models.User'>
print(user.id)            # 13982132
print(user.name)          # MIT Media Lab
print(user.screen_name)   # medialab
print(user.created_at)    # 2008-02-26 03:06:21
print(user.description)   # News from the MIT Media Lab
~~~

## Working with the JSON

~~~py
raw_tweet = tweet._json
print(type(raw_tweet))    # <class 'dict'>
~~~
