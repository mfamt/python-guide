import json
import os.path
import tweepy

def tweepy_client(credsfile):
    """
    Expects {credsfile} to be a filename for a JSON file in this format:
    {
      "consumer_key": "x",
      "consumer_secret": "y",
      "access_token": "z",
      "access_token_secret": "aa"
    }

    Returns an authenticated tweepy.API object
    """
    credsfile = os.path.expanduser(credsfile)
    creds = json.load(open(credsfile))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'],
      consumer_secret = creds['consumer_secret'])
    auth.set_access_token(creds['access_token'],
      creds['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)


def get_latest_timeline_tweet_text(credsfile):
    """
    Returns the latest text string from the authenticated user's
    timeline, or None if no tweet yet exists
    """
    t = tweepy_client(credsfile).user_timeline(count = 1, trim_user = True)
    if t[0]:
        return t[0].text

def send_tweet(txt, credsfile):
    """
    Sends out {txt} as a new tweet with the
    authenticated account from {credsfile}
    Returns the tweepy Response object
    """
    t = tweepy_client(credsfile)
    resp = t.update_status(status = txt)
    return resp
