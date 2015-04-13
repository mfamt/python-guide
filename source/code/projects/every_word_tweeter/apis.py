import json
import logging
import os.path
import tweepy
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('beholdeveryword.apis')


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
    t = tweepy_client(credsfile).user_timeline(count = 1, trim_user = True,
        exclude_replies = True, include_rts = False
    )
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
    return resp._json


def get_wikipedia_url_for_word(word):
    """
    contacts Wikipedia's API to see if an article with {word}.capitalize() exists
    Returns wikipedia URL with {word} as title if it does exist
     or None if not

    note: this method is pretty sloppy and assumes word is just a single word with
      all alphabet letters
    """
    wend_point = "http://en.wikipedia.org/w/api.php?format=json&action=query&prop=info&titles="
    title = word.capitalize()
    resp = requests.get(wend_point + title).json()
    if resp['query']['pages'].get('-1'):
        return None
    else:
        return "http://en.wikipedia.org/wiki/%s" % title

def get_biblehub_url_for_word(word):
    """
    Given {word} like "Abel"
      creates the biblehub.com topic URL:
       e.g. http://biblehub.com/topical/a/abel.html
      and checks to see if it exists (i.e. has a HTTP status of 200)

      Returns the biblehub.com URL or None
    """
    slug = word.lower()
    url = 'http://biblehub.com/topical/%s/%s.htm' % (slug[0], slug)
    resp = requests.head(url)
    return url if resp.status_code == 200 else None

