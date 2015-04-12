from apis import send_tweet, get_latest_timeline_tweet_text
from apis import get_wikipedia_url_for_word
from words import create_words_file, find_next_wordline
import json
import logging
import os.path
import re
TWITTER_CREDS = "~/.behold.twittercreds.json"
SOURCE_URL = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'
WORDS_FILENAME = "/tmp/biblewords.txt"

TWEET_TEMPLATE = "Behold %s and its %s Biblical %s!\n👼🙏😇😇😇"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('beholdeveryword.everyword')


def create_next_tweet_text(tweet_txt, words_filename):
    """
    Expects TWEET_TEMPLATE to be a String
    {tweet_txt} is a String. A regex is used to extract a particular
       {word}, and this is passed into words.find_next_wordline() to
       get the next [word, word_count] (e.g. {seq}) to tweet

    Returns a text string or None, depending on whether
      find_next_wordline() returned {seq} or None
    """
    new_tweet = None
    mtch = re.search('(?<=Behold )[A-Z]+', tweet_txt)
    word = mtch.group() if mtch else None
    seq = find_next_wordline(current_word = word, words_filename = words_filename)
    if seq is not None:
        word = seq[0].upper()
        tx = "appearances" if int(seq[1]) > 1 else 'appearance'
        new_tweet =  TWEET_TEMPLATE % (word, seq[1], tx)
        w_url = get_wikipedia_url_for_word(word)
        if w_url:
            new_tweet += "\n" + w_url

    return new_tweet


def dotweet(testing = False):
    """
    Downloads and creates Biblical word count (WORDS_FILE) if necessary.
    Gets latest tweet from a given account (TWITTER_SCREEN_NAME)
    Uses Tweepy to send a "Behold..." tweet

    Returns response object or None
    """
    create_words_file(source_url = SOURCE_URL, words_filename = WORDS_FILENAME,
        start_pt = '1:1', end_pt = 'END OF THE PROJECT GUTENBERG'
    )
    # Note: If the latest tweet isn't of the expected "Behold..." format,
    #   then the Twitter sequence will __start over__
    tweet_text = get_latest_timeline_tweet_text(credsfile = TWITTER_CREDS)
    logger.info("Latest tweet is: \"%s\"" % tweet_text)
    # Now formulate the next tweet to send out
    next_tweet = create_next_tweet_text(tweet_text, WORDS_FILENAME)
    if next_tweet is None:
        logger.warning("Nothing to tweet")
        return None
    else:
        logger.info("Tweeting: \"%s\"" % next_tweet)
        # send the tweet
        if testing == True:
            return next_tweet
        else:
            resp = send_tweet(next_tweet, credsfile = TWITTER_CREDS)
            return resp


if __name__ == "__main__":
    resp = dotweet()
    if type(resp) is dict:
        j = json.dumps(resp, indent = 2)
        print(j)
    else:
        print(resp)
