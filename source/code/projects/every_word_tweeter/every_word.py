import tweeter
import words
import json
import logging
import os.path
import re
TWITTER_CREDS = "~/.behold.twittercreds.json"
SOURCE_URL = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'
WORDS_FILENAME = "/tmp/biblewords.txt"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('beholdeveryword.everyword')


def extract_beheld_word(txt):
    """
    From a standard "Behold" tweet, extracts the all-caps word
    Returns extracted word, or None
    """
    m = re.search('(?<=Behold )[A-Z]+', txt)
    return m.group() if m else None



def create_next_tweet_text(tweet_txt, words_filename):
    """
    tweet_txt is text from a tweet that looks like:
       "Behold SOMEWORD and its 10 Biblical appearances"
    Extracts the "SOMEWORD" word, whether or not it exists
      and passes it to formulate_tweet_text

    Returns a text string or None, depending on find_next_wordline()
    """
    w = extract_beheld_word(tweet_txt)
    seq = words.find_next_wordline(current_word = w, words_filename = words_filename)
    if seq is not None:
        word = seq[0].upper()
        tx = "appearances" if int(seq[1]) > 1 else 'appearance'
        txt = "Behold %s and its %s Biblical %s!\n👼🙏😇😇😇" % (word, seq[1], tx)
        return txt


def dotweet():
    """
    Downloads and creates Biblical word count (WORDS_FILE) if necessary.
    Gets latest tweet from a given account (TWITTER_SCREEN_NAME)
    Uses Tweepy to send a "Behold..." tweet

    Returns response object
    """
    words.create_words_file(source_url = SOURCE_URL, words_filename = WORDS_FILENAME,
        start_pt = '1:1', end_pt = 'END OF THE PROJECT GUTENBERG'
    )
    tweet_text = tweeter.get_latest_timeline_tweet_text(credsfile = TWITTER_CREDS)
    logger.info("Latest tweet: \"%s\"" % tweet_text)
    next_tweet = create_next_tweet_text(tweet_text, WORDS_FILENAME)
    if next_tweet is None:
        logger.warning("Nothing to tweet")
    else:
        logger.info("Tweeting: \"%s\"" % next_tweet)
        # send the tweet
        resp = tweeter.send_tweet(next_tweet, credsfile = TWITTER_CREDS)
        return resp


if __name__ == "__main__":
    resp = dotweet()
    if resp:
        j = json.dumps(resp._json, indent = 2)
        print(j)
