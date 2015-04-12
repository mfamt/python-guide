import json
import os.path
from os import makedirs
DATA_DIR = '/tmp/data-hold/nyt-articles'
makedirs(DATA_DIR, exist_ok = True)
# pick beginning and end dates
d1 = '2014-01-01'
d2 = '2014-03-31'
for d in day_sequencer(d1, d2):
    fname = os.path.join(DATA_DIR, d + '.json')
    if not os.path.exists(fname):
        print("Gathering data for", fname)
        articles = get_nyt_articles_on_day(d)
        with open(fname, 'w') as j:
            j.write(json.dumps(articles, indent = 2))
