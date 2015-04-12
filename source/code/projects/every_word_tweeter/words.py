import os.path
import requests
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('beholdeveryword.words')


def create_words_file(source_url, words_filename, start_pt = "", end_pt = "", do_refresh = False):
    """
    Downloads latest Bible file and creates WORDS_FILE
    """
    # if it already exists, and no need to refresh it, then
    # just do nothing
    if(os.path.exists(words_filename)
             and os.path.getsize(words_filename) > 1000
             and do_refresh == False
    ):
        return
    # else, re-download, and re-make
    logger.info("Downloading text from %s" % source_url)
    text = requests.get(source_url).text.upper()
    a = text.index(start_pt)
    b = text.index(end_pt)
    words = re.findall("[A-Z]+", text[a:b])
    wordcounts = {}
    for word in words:
        if word not in wordcounts:
            wordcounts[word] = 1
        else:
            wordcounts[word] += 1

    with open(words_filename, "w") as f:
        for word, x in sorted(wordcounts.items()):
            f.write('%s,%s\n' % (word, x))
    logger.info("%s is %s bytes" % (words_filename, os.path.getsize(words_filename)))
    # return the path to the file
    return words_filename


def find_next_wordline(words_filename, current_word = None):
    """
    Finds line after the first match of current_word
    Returns a sequence/list, [word, word_count]
      or,
    if word is not found, or end of file,
       returns None
    """
    nextline = ''
    with open(words_filename) as f:
        if current_word is None:
            nextline = f.readline()
        else:
            for line in f:
                r = "^%s(?=,)" % current_word
                s = re.search(r,line)
                if s:
                    nextline = f.readline()
                    break
        if nextline is '':
            return None
        else:
            return nextline.strip().split(',')

